module Slackbots
  def self.speak(payload, hook_url)    
    script_success = `curl -X POST --data-urlencode 'payload=#{payload}' #{hook_url}`
    puts script_success
  end
  def 
end

