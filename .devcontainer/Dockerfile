FROM mcr.microsoft.com/devcontainers/cpp:noble

RUN apt-get update && apt-get install -y wget gnupg unzip curl
RUN curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor | sudo tee /usr/share/keyrings/google-chrome.gpg > /dev/null
RUN echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list > /dev/null
RUN apt-get update
RUN apt-get install -y google-chrome-stable
#RUN CHROME_VERSION=$(google-chrome --version | grep -oP "\d+\.\d+\.\d+\.\d+" | cut -d. -f1)
#RUN CHROMEDRIVER_VERSION=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROME_VERSION")
#RUN wget -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
RUN wget -O /tmp/chromedriver.zip https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/124.0.6367.91/linux64/chromedriver-linux64.zip
RUN unzip /tmp/chromedriver.zip -d /usr/local/bin/
RUN chmod +x /usr/local/bin/chromedriver
RUN pip install selenium pandas
    
