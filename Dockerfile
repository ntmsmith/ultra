FROM ultrateam/ultra:0.0.3
RUN git clone https://github.com/ntmsmith/ultra.git /root/ntmsmithultra/
WORKDIR /root/ntmsmithultra/
RUN pip install -r requirements.txt
CMD ["bash", "resources/startup/startup.sh"]
