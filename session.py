# Modul sesi untuk menyimpan dan membaca data sesi

_session = {}  # Variabel global untuk menyimpan sesi

def save_session(data):
    """Menyimpan sesi pengguna."""
    global _session
    _session = data

def get_session():
    """Mengembalikan data sesi pengguna."""
    return _session
