FROM ntmsmith/ultra:0.0.03
RUN git clone https://github.com/ntmsmith/ultra.git /root/ntmsmith/
WORKDIR /root/ntmsmith/
RUN pip install -r requirements.txt
CMD ["bash", "resources/startup/startup.sh"]
