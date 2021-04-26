FROM Ultrateam/Ultra:0.0.3
RUN git clone https://github.com/TeamUltra/Ultra.git /root/TeamUltra/
WORKDIR /root/TeamUltra/
RUN pip install -r requirements.txt
CMD ["bash", "resources/startup/startup.sh"]
