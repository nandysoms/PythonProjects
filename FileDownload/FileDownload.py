from urllib import request

file_url = r"http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv"


def download_file(url):
    resp = request.urlopen(url)
    csv_file = resp.read()
    print(csv_file)
    str_csv_file = str(csv_file)
    csv_lines = str_csv_file.split("\\r\\n")
    print(csv_lines)
    sav_csv_file = r'c:\users\nandy\desktop\test.csv'
    file = open(sav_csv_file, "w")
    for line in csv_lines:
        file.write(line + "\n")
    file.close()


download_file(file_url)
