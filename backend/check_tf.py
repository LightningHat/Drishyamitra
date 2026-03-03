import sys
try:
    import numpy as np
    import tensorflow as tf
    print(f"Python version: {sys.version}")
    print(f"Numpy version: {np.__version__}")
    print(f"TensorFlow version: {tf.__version__}")
    print("✅ System is READY for AI!")
except Exception as e:
    print(f"❌ Still failing. Error: {e}")