from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

# Folder sementara untuk simpan script yang masuk
UPLOAD_FOLDER = 'temp_scripts'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/execute', methods=['POST'])
def execute():
    if 'file' not in request.files:
        return "Error: None Files were sended."
    
    file = request.files['file']
    filename = file.filename
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    
    # Ambil ekstensi file (lua, py, mobj, dll)
    ext = filename.split('.')[-1].lower()
    
    try:
        # Logika eksekusi berdasarkan bahasa
        if ext == 'lua':
            cmd = ['lua', filepath]
        elif ext == 'py':
            cmd = ['python3', filepath]
        elif ext == 'mobj':
            # Contoh jika kamu sudah punya interpreter ModularOBJ
            cmd = ['./modularobj', filepath]
        else:
            return f"Error: Extenstion .{ext} Is not Supported!!"

        # Jalankan command dan ambil outputnya
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=10)
        return output.decode('utf-8')

    except subprocess.CalledProcessError as e:
        return f"Runtime Error:\n{e.output.decode('utf-8')}"
    except Exception as e:
        return f"System Error: {str(e)}"
    finally:
        # Hapus file setelah selesai agar server tidak penuh
        if os.path.exists(filepath):
            os.remove(filepath)

if __name__ == '__main__':
    # Server jalan di port 5000
    app.run(host='0.0.0.0', port=5000)
