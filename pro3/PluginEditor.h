/*
  ==============================================================================

    This file was auto-generated by the Introjucer!

    It contains the basic startup code for a Juce application.

  ==============================================================================
*/

#ifndef PLUGINEDITOR_H_INCLUDED
#define PLUGINEDITOR_H_INCLUDED

#include "../JuceLibraryCode/JuceHeader.h"
#include "PluginProcessor.h"

//==============================================================================
/**
*/
class FilterAudioProcessorEditor  : public AudioProcessorEditor, 
                                    public SliderListener
{
public:
    FilterAudioProcessorEditor (FilterAudioProcessor* ownerFilter);
    ~FilterAudioProcessorEditor();
private:
   Slider slider;

    //==============================================================================
    // This is just a standard Juce paint method...
    void paint (Graphics& g);
    void resized() override;
    void sliderValueChanged(Slider*) override;
};


#endif  // PLUGINEDITOR_H_INCLUDED
