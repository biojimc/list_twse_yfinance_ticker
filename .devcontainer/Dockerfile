FROM mcr.microsoft.com/devcontainers/cpp:noble

RUN apt-get update && apt-get install -y wget gnupg unzip curl python3 python3-pip
RUN curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor | sudo tee /usr/share/keyrings/google-chrome.gpg > /dev/null
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list > /dev/null
RUN apt-get update
RUN apt-get install -y google-chrome-stable
RUN CHROME_VERSION=$(google-chrome --version | grep -oP "\d+\.\d+\.\d+\.\d+") && \
  echo $CHROME_VERSION && \
  wget -O /tmp/chromedriver.zip "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${CHROME_VERSION}/linux64/chromedriver-linux64.zip"
RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/
RUN mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver
RUN pip3 install --break-system-packages selenium pandas lxml html5lib beautifulsoup4

    
