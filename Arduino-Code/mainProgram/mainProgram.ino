#include <Adafruit_GFX.h>    // Core graphics library
#include <Adafruit_TFTLCD.h> // Hardware-specific library
#include <TouchScreen.h>

#define LCD_CS A3
#define LCD_CD A2
#define LCD_WR A1
#define LCD_RD A0

#define LCD_RESET A4

#define	BLACK   0x0000
#define	BLUE    0x001F
#define	RED     0xF800
#define	GREEN   0x07E0
#define CYAN    0x07FF
#define MAGENTA 0xF81F
#define YELLOW  0xFFE0
#define WHITE   0xFFFF

#define ILI9341_BLACK       0x0000      /*   0,   0,   0 */
#define ILI9341_NAVY        0x000F      /*   0,   0, 128 */
#define ILI9341_DARKGREEN   0x03E0      /*   0, 128,   0 */
#define ILI9341_DARKCYAN    0x03EF      /*   0, 128, 128 */
#define ILI9341_MAROON      0x7800      /* 128,   0,   0 */
#define ILI9341_PURPLE      0x780F      /* 128,   0, 128 */
#define ILI9341_OLIVE       0x7BE0      /* 128, 128,   0 */
#define ILI9341_LIGHTGREY   0xC618      /* 192, 192, 192 */
#define ILI9341_DARKGREY    0x7BEF      /* 128, 128, 128 */
#define ILI9341_BLUE        0x001F      /*   0,   0, 255 */
#define ILI9341_GREEN       0x07E0      /*   0, 255,   0 */
#define ILI9341_CYAN        0x07FF      /*   0, 255, 255 */
#define ILI9341_RED         0xF800      /* 255,   0,   0 */
#define ILI9341_MAGENTA     0xF81F      /* 255,   0, 255 */
#define ILI9341_YELLOW      0xFFE0      /* 255, 255,   0 */
#define ILI9341_WHITE       0xFFFF      /* 255, 255, 255 */
#define ILI9341_ORANGE      0xFD20      /* 255, 165,   0 */
#define ILI9341_GREENYELLOW 0xAFE5      /* 173, 255,  47 */
#define ILI9341_PINK        0xF81F

#define BUTTON_X 40
#define BUTTON_Y 100
#define BUTTON_W 60
#define BUTTON_H 30
#define BUTTON_SPACING_X 20
#define BUTTON_SPACING_Y 20
#define BUTTON_TEXTSIZE 2

#define TEXT_X 10
#define TEXT_Y 10
#define TEXT_W 220
#define TEXT_H 50
#define TEXT_TSIZE 3
#define TEXT_TCOLOR ILI9341_MAGENTA
#define TEXT_LEN 5
char textfield[TEXT_LEN+1] = "";
uint8_t textfield_i=0;

#define YP A3
#define XM A2
#define YM 9
#define XP 8

#define TS_MINX 180
#define TS_MINY 170
#define TS_MAXX 920
#define TS_MAXY 930

#define STATUS_X 10
#define STATUS_Y 65

Adafruit_TFTLCD tft(LCD_CS, LCD_CD, LCD_WR, LCD_RD, LCD_RESET);
TouchScreen ts = TouchScreen(XP, YP, XM, YM, 300);

Adafruit_GFX_Button buttons[15];
/* create 15 buttons, in classic candybar phone style */
char buttonlabels[15][5] = {"Go", "Lock", "Del", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "0", "#" };
uint16_t buttoncolors[15] = {ILI9341_DARKGREEN, ILI9341_BLACK, ILI9341_RED, 
                             ILI9341_BLUE, ILI9341_BLUE, ILI9341_BLUE, 
                             ILI9341_BLUE, ILI9341_BLUE, ILI9341_BLUE, 
                             ILI9341_BLUE, ILI9341_BLUE, ILI9341_BLUE, 
                             ILI9341_ORANGE, ILI9341_BLUE, ILI9341_ORANGE};
                             
char sending[16] = "sending data...";
int input;
boolean justSent = false;

void setup(void) {
  Serial.begin(9600);
  
  tft.reset();
  
  uint16_t identifier = tft.readID();
  
  if(identifier == 0x9325) {
  /*} else if(identifier == 0x9328) {
  } else if(identifier == 0x4535) {;
  } else if(identifier == 0x7575) {
  } else if(identifier == 0x9341) {
  } else if(identifier == 0x8357) {*/
  } else if(identifier==0x0101) {     
      identifier=0x9341;
  }
  else if(identifier==0x1111) {     
      identifier=0x9328;
  }
  else {
    identifier=0x9328;
  }

  tft.begin(identifier);
  tft.setRotation(0);
  tft.fillScreen(BLACK);
  
  // create buttons
  for (uint8_t row=0; row<5; row++) {
    for (uint8_t col=0; col<3; col++) {
      buttons[col + row*3].initButton(&tft, BUTTON_X+col*(BUTTON_W+BUTTON_SPACING_X), 
                 BUTTON_Y+row*(BUTTON_H+BUTTON_SPACING_Y),    // x, y, w, h, outline, fill, text
                  BUTTON_W, BUTTON_H, ILI9341_WHITE, buttoncolors[col+row*3], ILI9341_WHITE,
                  buttonlabels[col + row*3], BUTTON_TEXTSIZE); 
      buttons[col + row*3].drawButton();
    }
  }
  
  // create 'text field'
  tft.drawRect(TEXT_X, TEXT_Y, TEXT_W, TEXT_H, ILI9341_WHITE);
  
  Serial.println("---start---");
}

// Print something in the mini status bar with either flashstring
void status(const __FlashStringHelper *msg) {
  tft.fillRect(STATUS_X, STATUS_Y, 240, 8, ILI9341_BLACK);
  tft.setCursor(STATUS_X, STATUS_Y);
  tft.setTextColor(ILI9341_WHITE);
  tft.setTextSize(1);
  tft.print(msg);
}

// or charstring
void status(char *msg) {
  tft.fillRect(STATUS_X, STATUS_Y, 240, 8, ILI9341_BLACK);
  tft.setCursor(STATUS_X, STATUS_Y);
  tft.setTextColor(ILI9341_WHITE);
  tft.setTextSize(1);
  tft.print(msg);
}

#define MINPRESSURE 10
#define MAXPRESSURE 1000

void loop(void) {
  
  digitalWrite(13, HIGH);
  TSPoint p = ts.getPoint();
  digitalWrite(13, LOW);
  
  pinMode(XM, OUTPUT);
  pinMode(YP, OUTPUT);
  
  if (p.z > MINPRESSURE && p.z < MAXPRESSURE) {
    // scale from 0->1023 to tft.width
    p.x = tft.width() - map(p.x, TS_MINX, TS_MAXX, tft.width(), 0);
    p.y = map(p.y, TS_MINY, TS_MAXY, tft.height(), 0);
  }
   
  // go through all the buttons, checking if they were pressed
  for (uint8_t b=0; b<15; b++) {
    if (buttons[b].contains(p.x, p.y)) {
      buttons[b].press(true);  // tell the button it is pressed
    } else {
      buttons[b].press(false);  // tell the button it is NOT pressed
    }
  }

  // ask the buttons if their state has changed
  for (uint8_t b=0; b<15; b++) {
    if (buttons[b].justReleased()) {
      buttons[b].drawButton();  // draw normal
    }
    
    if (buttons[b].justPressed()) {
        buttons[b].drawButton(true);  // draw invert!
        
        // if a numberpad button, append the relevant # to the textfield
        if (b >= 3) {
          if (textfield_i < TEXT_LEN) {
            textfield[textfield_i] = buttonlabels[b][0];
            textfield_i++;
	    textfield[textfield_i] = 0; // zero terminate
          }
          status(F(""));
        }

        // del button! delete char
        if (b == 2) {
          textfield[textfield_i] = 0;
          /*if (textfield > 0) {
            textfield_i--;
            textfield[textfield_i] = ' ';
          }*/
          if (strlen(textfield) > 0) {
            textfield_i--;
            textfield[textfield_i] = ' ';
          }
          status(F(""));
        }

        // update the current text field
        tft.setCursor(TEXT_X + 2, TEXT_Y+10);
        tft.setTextColor(TEXT_TCOLOR, ILI9341_BLACK);
        tft.setTextSize(TEXT_TSIZE);
        tft.print(textfield);

        // TODO extra button
        if (b == 1) {
          status(F("Locked"));
        }
        
        if (b == 0) {
          status(F("Sending"));
          Serial.println(sending);
          Serial.println(textfield);
          
          justSent = true;
        }
        
      delay(100); // UI debouncing
    }
    
    if (justSent && Serial.available() > 0) {
      input = Serial.read();
      
      if (input == 48) { // 48 is ASCII for 0 (zero)
        status(F("Invalid ID. Try Again."));
        Serial.println("Invalid ID. Try Again.");
        justSent = false;
      }
      
      if (input == 49) { // 49 is ASCII for 1 (one)
        status(F("Approved. Be free."));
        Serial.println("Approved. Be free.");
        justSent = false;
      }
    }
  }
}
