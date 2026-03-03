const { Client, LocalAuth, MessageMedia } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

const client = new Client({
    authStrategy: new LocalAuth(), // Saves your login session
    puppeteer: { args: ['--no-sandbox'] }
});

// 1. Generate QR Code in terminal for scanning
client.on('qr', (qr) => {
    console.log('SCAN THIS QR CODE WITH WHATSAPP:');
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('✅ WhatsApp Web is ready!');
});

// 2. Create an API endpoint for Flask to call
app.post('/send-image', async (req, res) => {
    const { phone, caption, imagePath } = req.body;
    
    try {
        const chatId = phone.includes('@c.us') ? phone : `${phone}@c.us`;
        const media = MessageMedia.fromFilePath(imagePath);
        
        await client.sendMessage(chatId, media, { caption: caption });
        res.status(200).json({ success: true, message: 'Image sent!' });
    } catch (err) {
        res.status(500).json({ success: false, error: err.message });
    }
});

app.listen(3001, () => {
    console.log('WhatsApp Service running on http://localhost:3001');
});

client.initialize();