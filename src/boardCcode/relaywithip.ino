int RELAY1 = D0;
int RELAY2 = D1;
char ip[15];

void setup()
{
   //Initilize the relay control pins as output
   pinMode(RELAY1, OUTPUT);
   pinMode(RELAY2, OUTPUT);
   // Initialize all relays to an OFF state
   digitalWrite(RELAY2, HIGH);
   digitalWrite(RELAY1, LOW);
   
   //register the Particle function
   Particle.function("relay", relayControl);\
   Particle.variable("IpAddr", ip);
   Particle.subscribe("particle/device/ip" , handler);
   Particle.publish("particle/device/ip");

}

void loop()
{
   // This loops for ever
}

void handler(const char *topic, const char *data)
{
    //sprintf(ip, "%s", data);
    strcpy(ip, data);
}

// command format r1,HIGH
int relayControl(String command)
{
    digitalWrite(RELAY2, 0);
    delay(1000);
    digitalWrite(RELAY1, 1);
    delay(500);
    digitalWrite(RELAY1, 0);
    
    return 1;
}