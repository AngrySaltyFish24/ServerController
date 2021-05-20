int RELAY1 = D0;

void setup()
{
   //Initilize the relay control pins as output
   pinMode(RELAY1, OUTPUT);
   // Initialize all relays to an OFF state
   digitalWrite(RELAY1, LOW);

   //register the Particle function
   Particle.function("relay", relayControl);
}

void loop()
{
   // This loops for ever
}

// command format r1,HIGH
int relayControl(String command)
{
    digitalWrite(0, 1);
    delay(500);
    digitalWrite(0, 0);
    
    return 1;
}