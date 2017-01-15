require 'json'

module Slackbots
  def self.speak(payload, hook_url)    
    script_success = `curl -X POST --data-urlencode 'payload=#{payload.to_json}' #{hook_url}`
    puts script_success
  end
  def create_payload(text, channel, username, icon_url)
    payload = {"text": text, "channel": channel, "username": username, "icon_url": icon_url}
    return payload
  end
  def 
end

