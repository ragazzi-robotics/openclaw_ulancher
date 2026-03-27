import subprocess

def run_query(query):
    try:
        subprocess.run(query, shell=True)
    except:
        result = subprocess.check_output(
            ["openclaw", "run", query],
            text=True
        )
        subprocess.run(result, shell=True)
