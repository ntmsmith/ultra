FROM ntmsmith/
RUN git clone https://github.com/ntmsmith/ultra /root/ntmsmith/
WORKDIR /root/ntmsmith/
RUN pip install -r requirements.txt
CMD ["bash", "resources/startup/startup.sh"]
