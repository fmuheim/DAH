// works with fft4.py run on R-Pi
// sends data through USB after having them buffered
// sampling rate is set through USB
// achieved rates about 100ksps

// see also
// http://www.instructables.com/id/Girino-Fast-Arduino-Oscilloscope/?ALLSTEPS

#ifndef cbi
#define cbi(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif
#ifndef sbi
#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

void setup()  { 
  Serial.begin(115200); // 115200, 230400, 460800, 500000, 576000, 921600, 1000000
//  noInterrupts();           // disable all interrupts
  TCCR1A = 0; // zero the counter lower byte
  TCCR1B = 0; // zero the counter higher byte
  TCCR1B |= (1 << CS11) ;  // set timer rate to 1/8 of the CPU clock (16MHz)  = 2MHz
  TCNT1=0 ; // zero the timer
  
  DDRD = DDRD&B00000011; // set pins 2-7 as inputs
  DDRB = B00111111 ; // sets pins  8-13 as outputs
//  pinMode(13, OUTPUT);

// set ADC prescale to 16
  sbi(ADCSRA,ADPS2) ;
  cbi(ADCSRA,ADPS1) ;
  cbi(ADCSRA,ADPS0) ;
  
      // ADPS2 ADPS1 ADPS0 Division Factor
        // 0 0 0 2
        // 0 0 1 2
        // 0 1 0 4
        // 0 1 1 8
        // 1 0 0 16
        // 1 0 1 32
        // 1 1 0 64
        // 1 1 1 128
} 

unsigned int t1=0,t2 ;
//int state=1 ;
const int ln=1600 ;
byte buf[ln] ;
//int ito=0, ifrom=0 ;

void loop()  { 
  unsigned int c, del, i ;
  byte b ;

  while (Serial.available()==0) ;
  b=Serial.read() ; del=b<<2 ; // set time delay
  while (Serial.available()==0) ;
  b=Serial.read() ; ADCSRA&=B11111000 ; ADCSRA|=(b&B00000111) ; // set ADC time prescaler
  
//  del=(PIND&B11111100)<<2 ;

  noInterrupts();  

  for (i=0;i<ln;i++) {
    if (TCNT1>10000) { TCNT1-=10000 ; t1-=10000 ; } // make sure the timer does not overflow
    while ((t2=TCNT1)<t1+del) ;
    t1=t2 ;
    c=analogRead(A0);
    c=c>>2 ; buf[i]=c ;
  }

  interrupts();

  Serial.write(buf,ln) ;
  PORTB^=B00100000 ;  
}

