/*
  ==============================================================================

    This file was auto-generated!

    It contains the basic startup code for a Juce application.

  ==============================================================================
*/

#include "PluginProcessor.h"
#include "PluginEditor.h"

const float pi = 3.14159265359;
float wave[FLANGELEN];
int flangeSpeed = 10;

void makeWave(){
   float inc = pi / FLANGELEN;
   for (int i = 0; i < FLANGELEN; i++){
      wave[i] = sin(i * inc);
   }
}

void updateFlangeSpeed(double speed){
   flangeSpeed = 1000 * speed;
}
//==============================================================================
FilterAudioProcessor::FilterAudioProcessor()
{
}

FilterAudioProcessor::~FilterAudioProcessor()
{
}

//==============================================================================
const String FilterAudioProcessor::getName() const
{
    return JucePlugin_Name;
}

int FilterAudioProcessor::getNumParameters()
{
    return 0;
}

float FilterAudioProcessor::getParameter (int index)
{
    return 0.0f;
}

void FilterAudioProcessor::setParameter (int index, float newValue)
{
}

const String FilterAudioProcessor::getParameterName (int index)
{
    return String::empty;
}

const String FilterAudioProcessor::getParameterText (int index)
{
    return String::empty;
}

const String FilterAudioProcessor::getInputChannelName (int channelIndex) const
{
    return String (channelIndex + 1);
}

const String FilterAudioProcessor::getOutputChannelName (int channelIndex) const
{
    return String (channelIndex + 1);
}

bool FilterAudioProcessor::isInputChannelStereoPair (int index) const
{
    return true;
}

bool FilterAudioProcessor::isOutputChannelStereoPair (int index) const
{
    return true;
}

bool FilterAudioProcessor::acceptsMidi() const
{
   #if JucePlugin_WantsMidiInput
    return true;
   #else
    return false;
   #endif
}

bool FilterAudioProcessor::producesMidi() const
{
   #if JucePlugin_ProducesMidiOutput
    return true;
   #else
    return false;
   #endif
}

bool FilterAudioProcessor::silenceInProducesSilenceOut() const
{
    return false;
}

double FilterAudioProcessor::getTailLengthSeconds() const
{
    return 0.0;
}

int FilterAudioProcessor::getNumPrograms()
{
    return 0;
}

int FilterAudioProcessor::getCurrentProgram()
{
    return 0;
}

void FilterAudioProcessor::setCurrentProgram (int index)
{
}

const String FilterAudioProcessor::getProgramName (int index)
{
    return String::empty;
}

void FilterAudioProcessor::changeProgramName (int index, const String& newName)
{
}

//==============================================================================
void FilterAudioProcessor::prepareToPlay (double sampleRate, int samplesPerBlock)
{
    // Use this method as the place to do any pre-playback
    // initialisation that you need..
}

void FilterAudioProcessor::releaseResources()
{
    // When playback stops, you can use this as an opportunity to free up any
    // spare memory, etc.
}

void FilterAudioProcessor::processBlock (AudioSampleBuffer& buffer, MidiBuffer& midiMessages)
{
   int numSamples = buffer.getNumSamples();
   int flangeCount = 0;
   int offs;
   float ptotal = 0, ntotal = 0;

   makeWave();
   
    // This is the place where you'd normally do the guts of your plugin's
    // audio processing...
    for (int channel = 0; channel < getNumInputChannels(); ++channel)
    {
       
        float* channelData = buffer.getSampleData (channel);

        // ..do something to the data...
        for (int i = 0; i < numSamples; i++) {
           if (flangeCount >= FLANGELEN){
              flangeCount = 0;
           }
           offs = i + (wave[flangeCount] * flangeSpeed);
           if (offs < numSamples || offs >= 0) {
              channelData[i] = (0.5 * channelData[i]) + (0.5 * channelData[offs]);
              if (channelData[i] > 0.5)
                 channelData[i] = 0.5;
              else if (channelData[i] < -0.5)
                 channelData[i] = -0.5;
           }
           if (i > 2) {
              channelData[i - 1] = (channelData[i] + channelData[i - 2]) / 2;
           }
           flangeCount++;
        }
    }

    // In case we have more outputs than inputs, we'll clear any output
    // channels that didn't contain input data, (because these aren't
    // guaranteed to be empty - they may contain garbage).
    for (int i = getNumInputChannels(); i < getNumOutputChannels(); ++i)
    {
        buffer.clear (i, 0, buffer.getNumSamples());
    }
}

//==============================================================================
bool FilterAudioProcessor::hasEditor() const
{
    return true; // (change this to false if you choose to not supply an editor)
}

AudioProcessorEditor* FilterAudioProcessor::createEditor()
{
    return new FilterAudioProcessorEditor (this);
}

//==============================================================================
void FilterAudioProcessor::getStateInformation (MemoryBlock& destData)
{
    // You should use this method to store your parameters in the memory block.
    // You could do that either as raw data, or use the XML or ValueTree classes
    // as intermediaries to make it easy to save and load complex data.
}

void FilterAudioProcessor::setStateInformation (const void* data, int sizeInBytes)
{
    // You should use this method to restore your parameters from this memory block,
    // whose contents will have been created by the getStateInformation() call.
}

//==============================================================================
// This creates new instances of the plugin..
AudioProcessor* JUCE_CALLTYPE createPluginFilter()
{
    return new FilterAudioProcessor();
}
