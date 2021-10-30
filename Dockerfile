# Docker Tag Images, Using Python Slim Buster 3.9
FROM apiskinguserbot/kinguserbot:Buster
# ==========================================
#              USERBOT TELEGRAM
# ==========================================
RUN git clone -b Remix-Userbot https://github.com/Randi356/Remix-Userbot /home/Remix-Userbot \
    && chmod 777 /home/Remix-Userbot \
    && mkdir /home/Remix-Userbot/bin/

# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/Remix-Userbot/

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Randi356/Remix-Userbot/Remix-Userbot/requirements.txt
WORKDIR /home/Remix-Userbot/

# Finishim
CMD ["bash","./resource/startup/startup.sh"]
