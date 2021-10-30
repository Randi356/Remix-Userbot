# Docker Tag Images, Using Python Slim Buster 3.9
FROM apiskinguserbot/kinguserbot:Buster
# ==========================================
#              USERBOT TELEGRAM
# ==========================================
RUN git clone -b Remix-Userbot https://github.com/Randi356/Remix-Userbot /home/userbot \
    && chmod 777 /home/userbot \
    && mkdir /home/userbot/bin/

# Copies config.env (if exists)
COPY ./sample_config.env ./config.env* /home/userbot/

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Randi356/Remix-Userbot/Remix-Userbot/requirements.txt
WORKDIR /home/userbot/

# Finishim
CMD ["bash","./resource/startup/startup.sh"]
