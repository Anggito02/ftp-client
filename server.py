# FTP SERVER
import ftplib

def connect_server():
    # SERVER CONFIGURATION
    HOST = "localhost"
    PORT = 21
    USERNAME ="abcde"
    PASSWORD = "12345"

    # Create FTP client instance
    ftp = ftplib.FTP()

    # Connect to FTP server
    connectionResponse = ftp.connect(HOST, PORT)

    # Login to FTP server
    loginResponse = ftp.login(USERNAME, PASSWORD)

    return [connectionResponse, loginResponse, ftp]

# TO-DO [Tugas 3-FTP Server]
"""
[FTP-1]: Cetak nama dan versi FTP server

Expected Output:
vsFTPd 3.0.2
"""
def print_server_info():
    # Connect to server
    _, _, ftp = connect_server()

    # Get server info
    serverInfo = ftp.getwelcome()

    # Output
    print("[FTP-1] Nama dan versi FTP Server")
    print("-----")
    print(serverInfo)
    print()
    print("====================")
    print()

    # SERVER DISCONNECT
    ftp.quit()

"""
[FTP-2]: Cetak sistem yang diemulasikan FTP server

Expected Output:
220 (vsFTPd 3.0.2)
331 Please specify the password.
230 Login successful.
215 UNIX Type: L8
221 Goodbye.
"""
def print_emulated_system():
    # Connect to server
    connectionResponse, loginResponse, ftp = connect_server()

    # Get emulated server info
    emulatedSystemInfo = ftp.sendcmd("SYST")

    # Output
    print("[FTP-2] Sistem yang diemulasikan FTP Server")
    print("-----")
    print(connectionResponse)
    print(loginResponse)
    print(emulatedSystemInfo)
    # SERVER DISCONNECT
    print(ftp.quit())
    print()
    print("====================")
    print()

"""
[FTP-3]: Cetak daftar file dan direktori di home direktori FTP server

Expected Output:
directory-name
.bash_logout
.bashrc
.profile
"""
def print_dir_list():
    # Connect to server
    _, _, ftp = connect_server()

    # Change working directory to ./home
    ftp.cwd("home")

    # Get directory list
    fileDirList = ftp.nlst()

    # Outputx
    print("[FTP-3] Daftar file dan direktori di home direktori FTP server")
    print("-----")
    print("directory-name")
    for file in fileDirList:
        print(f".{file}")
    print()
    print("====================")
    print()

    # SERVER DISCONNECT
    ftp.quit()

"""
[FTP-4]: Unggahlah sebuah file ke FTP server.

Expected output:
220 (vsFTPd 3.0.2)
331 Please specify the password.
230 Login successful.
200 Switching to ASCII mode.
150 Ok to send data.
226 Transfer complete.
221 Goodbye.
"""
def upload_file(fileDirectory, remoteDirectory):
    # Connect to server
    connectionResponse, loginResponse, ftp = connect_server()

    # Change workin directory
    ftp.cwd(remoteDirectory)

    # Switch to ASCII mode
    asciiResponse = ftp.sendcmd("TYPE A")

    # Upload file
    localFile = open(fileDirectory, "rb")
    fileName = fileDirectory.split("/")[-1]
    uploadResponse =  ftp.storbinary("STOR " + fileName, localFile)

    # Output
    print("[FTP-4] Unggah file")
    print("-----")
    print(connectionResponse)
    print(loginResponse)
    print(asciiResponse)
    print(uploadResponse)
    print(ftp.quit())
    print()
    print("====================")
    print()

"""
[FTP-5]: Buatlah sebuah direktori dengan nama "test"

Expected output:
220 (vsFTPd 3.0.2)
331 Please specify the password.
230 Login successful.
257 "/test" created
221 Goodbye.
"""
def make_directory(newDirectoryPath):
    # Connect to server
    connectionResponse, loginResponse, ftp = connect_server()

    # Print current directory

    # Make directory
    makeDirectoryResponse = ftp.mkd(newDirectoryPath)

    # Output
    print("[FTP-5] Membuat direktori")
    print("-----")
    print(connectionResponse)
    print(loginResponse)
    print(f'"{makeDirectoryResponse}" created')
    print(ftp.quit())
    print()
    print("====================")
    print()

"""
[FTP-6]: Cetaklah direktori yang aktif saat ini di home directory pada FTP server

Expected output:
220 (vsFTPd 3.0.2)
331 Please specify the password.
230 Login successful.
257 "/"
221 Goodbye.
"""
def print_current_directory():
    # Connect to server
    connectionResponse, loginResponse, ftp = connect_server()

    # Get current directory
    currentDirectory = ftp.pwd()

    # Output
    print("[FTP-6] Direktori saat ini")
    print("-----")
    print(connectionResponse)
    print(loginResponse)
    print(f'"{currentDirectory}"')
    print(ftp.quit())
    print()
    print("====================")
    print()

"""
[FTP-7]: Gantilah nama direktori "test" yang dibuat pada soal FTP-5 dengan "test2"

Expected output:
220 (vsFTPd 3.0.2)
331 Please specify the password.
230 Login successful.
350 Ready for RNTO.
250 Rename successful.
221 Goodbye.
"""
def rename_dir(currDirectory, newDirectory):
    # Connect to server
    connectionResponse, loginResponse, ftp = connect_server()

    # Rename a directory
    renameResponse = ftp.rename(currDirectory, newDirectory)

    # Output
    print("[FTP-7] Mengganti nama direktori")
    print("-----")
    print(connectionResponse)
    print(loginResponse)
    print(renameResponse)
    print(ftp.quit())
    print()
    print("====================")
    print()

"""
[FTP-8]: Hapuslah direktori "test2" yang diproses pada soal FTP-7

Expected output:
250 Remove directory operation successful.
"""
def remove_dir(directory):
    # Connect to server
    _, _, ftp = connect_server()

    # Remove directory
    removeDirResponse = ftp.rmd(directory)

    # Output
    print("[FTP-8] Menghapus direktori")
    print("-----")
    print(removeDirResponse)
    print()
    print("====================")
    print()

if __name__ == "__main__":
    # [FTP-1]
    print_server_info()

    # [FTP-2]
    print_emulated_system()

    # [FTP-3]
    print_dir_list()

    # [FTP-4]
    # upload_file("./local/404.html", "/home/documents")

    # [FTP-5]
    make_directory("/home/test")

    # [FTP-6]
    print_current_directory()

    # [FTP-7]
    rename_dir("/home/test", "/home/test2")

    # [FTP-8]
    remove_dir("/home/test2")

    print("FTP Server disconnected...")