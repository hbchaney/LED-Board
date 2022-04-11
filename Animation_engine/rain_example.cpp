#include <iostream>
#include <fstream> //there are three classes ifstream ofstream and fstream
#include <string>
#include <stdlib.h>
using namespace std;

//this example works by storing a frame of rain in memory and add to a file 
//the frame is then updated 

class line{ 

    char* ptr; //points to the char arr 
    int sz = 64;
    public: 

    line () { 
        //initializes line with 64 empty spaces 
        ptr = new char[64];
        for (int i=0; i < sz; i++) {
            ptr[i] = '0'; 
            
        }
    } 

    ~line () { 
        delete ptr; 
    }

    char& index (int location) { 
        return ptr[location] ; 
    }
    const char& index(int location) const { 
        return ptr[location] ; 
    }

};

class frame { 
    
    int sz = 64;
    line* ls; 
    int frame_num; 

    public: 
    
    frame (int f=1) : frame_num{f} {
        ls = new line[64]; 
    } 
    ~frame () {
        delete ls; 
    }

    friend ostream& operator<< (ostream&,const frame&);

    char& index (int f_location,int l_location) { 
        return ls[f_location].index(l_location);
    }

    const char& index (int f_location,int l_location) const { 
        return ls[f_location].index(l_location);
    }

    //updates the frame number of frame 
    void frame_update (int num=0) { 
        if (num == 0) { 
            frame_num++; 
        }
        else { 
            frame_num = num; 
        }

    }
    int framer () const { 
        return frame_num; 
    }

};

ostream& operator<< (ostream& os,const frame& f) { 
    os << f.framer() << endl; 
    for (int i=0; i<64;i++ ) { 
        for (int j=0; j<64; j++) { 
            os << f.index(i,j) << ' ';
        } 
        os << endl; 
    }
    return os; 
}
 

void rain_upper(frame& fr) { 

    //first line 
    char rain = '7'; 
    char snow = '8'; 

    for (int i=0; i<64; i++) { 

    
        int random = rand() % 100;
        if (random > 85 && random <= 95) { 
            fr.index(0,i) = rain;
        }
        else if (random > 95) {
            fr.index(0,i) = snow;
        }
        else {
            fr.index(0,i) = '0';
        }
    }
    fr.frame_update(); 

} 

void rain_lower(frame& fr) { 

    for (int i = 63; i > 0; i--) { 
        for (int j = 0; j < 64; j++) { 
            fr.index(i,j) = fr.index(i-1,j); 
        }
    }
    fr.frame_update(); 

}

void to_file(string file_name,int num_frames)  { 
    ofstream gif_raw; 
    gif_raw.open(file_name);
    frame gif; 

    gif_raw << gif; 

    for (int i=0; i < (num_frames/3) ; i++) { 
        rain_upper(gif); 
        gif_raw << gif; 

        rain_lower(gif); 
        gif_raw << gif; 
        rain_lower(gif); 
        gif_raw << gif; 
    }

    gif_raw.close(); 



    
}



int main () { 

    to_file("rain_making.gif_raw",400); 

    return 0; 

}