import subprocess

def install_package(pkg: str) -> str:
    try:
        subprocess.check_call(["pip", "install", pkg])
        return f"✅ Installed {pkg}"
    except Exception as e:
        return f"❌ Failed to install {pkg}: {str(e)}"