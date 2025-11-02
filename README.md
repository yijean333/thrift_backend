# thrift-market

curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
  && echo "deb https://ngrok-agent.s3.amazonaws.com bookworm main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list \
  && sudo apt update \
  && sudo apt install ngrok

  **

  ngrok config add-authtoken 30oOnZa6unxi8on6V44IyadpvOV_5jfZeUkJ8kLbQZHKJP2gH

  **

  ngrok http 8000
