import java.io.*;
import java.util.Random;

public class mixUp {

   public static void main(String[] args) {
      try {
         //general use variables
         int fps = 44100;
         int length = 30;
         Random rng = new Random();
         int rNum;
         
         //create files to read and write
         File fIn = new File(args[0]);
         File fOut = new File(args[1]);
         
         //open in file as wav
         WavFile wavIn = WavFile.openWavFile(fIn);
         
         //get values
         long frames = wavIn.getNumFrames();
         int chan = wavIn.getNumChannels();
         int vBits = wavIn.getValidBits();
         int dur = ((int)frames/fps) - 1;
         
         //open file to make as wav
         WavFile wavOut = WavFile.newWavFile(fOut, chan, fps * length, vBits, fps);
         
         //make buffer
         double[] buf = new double[fps * chan];
         
         //Pick a random 1 second clip from the song and write it
         for(int i = 0; i < length; i++) {
            rNum = rng.nextInt(dur);
            for(int j = 0; j < rNum; j++) {
               wavIn.readFrames(buf, fps);
            }
            wavOut.writeFrames(buf, fps);
            wavIn.close();
            wavIn = WavFile.openWavFile(fIn);
         }
         
         wavIn.close();
         wavOut.close();
      }
      catch(Exception x) {
         System.out.println(x);
      }
   }
   
}