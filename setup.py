config_content = """
instances:
  master:
    sonarr:
      base_url: "http://localhost:8989"
      api_key: "API_KEY"
    radarr:
      base_url: "http://localhost:7878"
      api_key: "API_KEY"
  extras:
    sonarr:
      - name: "4k-sonarr"
        base_url: "http://localhost:8998"
        api_key: "API_KEY"
    radarr:
      - name: "4k-radarr"
        base_url: "http://localhost:7887"
        api_key: "API_KEY"

settings:
  export_path: "./exports"
"""

with open('config.yml', 'w') as file:
    file.write(config_content)