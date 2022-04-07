import streamlit as st

import pandas as pd
import numpy as np

st.title("Prediction Using LSTM model")

st.subheader("About LSTM model :")
st.write("LSTM networks are an extension of recurrent neural networks (RNNs) mainly introduced to handle situations where RNNs fail. Talking about RNN, it is a network that works on the present input by taking into consideration the previous output (feedback) and storing in its memory for a short period of time (short-term memory). Out of its various applications, the most popular ones are in the fields of speech processing, non-Markovian control, and music composition. Nevertheless, there are drawbacks to RNNs. First, it fails to store information for a longer period of time. At times, a reference to certain information stored quite a long time ago is required to predict the current output. But RNNs are absolutely incapable of handling such “long-term dependencies”. Second, there is no finer control over which part of the context needs to be carried forward and how much of the past needs to be ‘forgotten’. Other issues with RNNs are exploding and vanishing gradients (explained later) which occur during the training process of a network through backtracking. Thus, Long Short-Term Memory (LSTM) was brought into the picture. It has been so designed that the vanishing gradient problem is almost completely removed, while the training model is left unaltered. Long time lags in certain problems are bridged using LSTMs where they also handle noise, distributed representations, and continuous values. With LSTMs, there is no need to keep a finite number of states from beforehand as required in the hidden Markov model (HMM). LSTMs provide us with a large range of parameters such as learning rates, and input and output biases. Hence, no need for fine adjustments. The complexity to update each weight is reduced to O(1) with LSTMs, similar to that of Back Propagation Through Time (BPTT), which is an advantage.")

st.subheader("LSTM mechanism :")
st.write("1. Forgetting Mechanism:  Forget all scene related information that is not worth remembering ")
st.write("2. Saving Mechanism:  Save information that is important and can help in the future.Now that we know when to use LSTMs, let’s discuss the basics of it.")

st.subheader("The architecture of LSTM:")
st.write("1. LSTMs deal with both Long Term Memory (LTM) and Short Term Memory (STM) and for making the calculations simple and effective it uses the concept of gates.")
st.write("2. Forget Gate: LTM goes to forget gate and it forgets information that is not useful.")
st.write("3. Learn Gate: Event ( current input ) and STM are combined together so that necessary information that we have recently learned from STM can be applied to the current input.") 
st.write("4. Remember Gate: LTM information that we haven’t forget and STM and Event are combined together in Remember gate which works as updated LTM. Use Gate: This gate also uses LTM, STM, and Event to predict the output of the current event which works as an updated STM.")
st.image("Images//LSTM.png")
st.video("https://www.youtube.com/watch?v=5dMXyiWddYs")




def main():
    st.title("Prediction_Page")
