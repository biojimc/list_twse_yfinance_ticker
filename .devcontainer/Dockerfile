FROM mcr.microsoft.com/devcontainers/cpp:noble

RUN apt-get update && \
    # 安裝 Chrome 和相依套件
    apt install -y wget gnupg unzip curl
    
    # 加入 Google Chrome GPG key & repo
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
    sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
    apt update && apt install -y google-chrome-stable

    # 安裝 ChromeDriver（版本需與 Chrome 對應）
    CHROME_VERSION=$(google-chrome --version | grep -oP "\d+\.\d+\.\d+\.\d+" | cut -d. -f1)
    CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION")
    wget -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
    unzip /tmp/chromedriver.zip -d /usr/local/bin/
    chmod +x /usr/local/bin/chromedriver

    # 安裝 Python 套件
    pip install selenium pandas
    
