const { Client, LocalAuth, MessageMedia } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const express = require('express');
const app = express();

app.use(express.json());

const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: { 
        headless: true,
        args: ['--no-sandbox', '--disable-setuid-sandbox'] 
    }
});

client.on('qr', qr => qrcode.generate(qr, { small: true }));
client.on('ready', () => console.log('✅ WhatsApp Web Ready!'));

app.post('/send-photo', async (req, res) => {
    const { phone, caption, imagePath } = req.body;
    
    if (!client.info) return res.status(503).json({ success: false, error: "WhatsApp not authenticated" });

    try {
        const chatId = phone.includes('@c.us') ? phone : `${phone}@c.us`;
        const media = MessageMedia.fromFilePath(imagePath);
        
        const message = await client.sendMessage(chatId, media, { caption });
        
        // Check if message was actually acknowledged
        if (message.id.fromMe) {
            res.status(200).json({ success: true, messageId: message.id.id });
        } else {
            res.status(500).json({ success: false, error: "Message failed to send" });
        }
    } catch (err) {
        res.status(500).json({ success: false, error: err.message });
    }
});

app.listen(3001, () => console.log('WhatsApp Microservice on http://localhost:3001'));
client.initialize();