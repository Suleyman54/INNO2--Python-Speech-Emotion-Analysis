import pandas as pd
import librosa
import librosa.display
import numpy as np
import tensorflow as tf

import os


def predict():
    # class_dict5 = {
    #     0: "male_positive",
    #     1: "female_positive",
    #     2: "male_negative",
    #     3: "female_negative",
    # }
    class_dict4 = {
        0: "male_positive",
        1: "female_positive",
        2: "male_neutral",
        3: "female_neutral",
        4: "male_negative",
        5: "female_negative",
    }
    # class_dict6 = {
    #     0: "negative",
    #     1: "neutral",
    #     2: "positive"
    # }
    #
    # pred_to_class = {
    #     0: "female_angry",
    #     1: "female_calm",
    #     2: "female_fearful",
    #     3: "female_happy",
    #     4: "female_sad",
    #     5: "male_angry",
    #     6: "male_calm",
    #     7: "male_fearful",
    #     8: "male_happy",
    #     9: "male_sad"
    # }

    group_emotion_dict = {}

    model_filename = '../models/saved_models/Emotion_Voice_Detection_Model4.h5'

    loaded_model = tf.keras.models.load_model(model_filename)

    for (dirpath, dirnames, filenames) in os.walk("../src/audio/temp_frag"):
        for file_name in filenames:
            frag_emotion_dict = {
                0: 0,
                1: 0,
                2: 0
            }
            # all_emotion_dict["chunk" + str(iteration)] = {}
            X, sample_rate = librosa.load(os.path.join(dirpath, file_name),
                                          res_type='kaiser_fast',
                                          duration=2.5,
                                          sr=22050 * 2,
                                          offset=0.50)
            sample_rate = np.array(sample_rate)
            mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=13), axis=0)
            livedf2 = pd.DataFrame(data=mfccs)
            livedf3 = livedf2.stack().to_frame().T
            twodim = np.expand_dims(livedf3, axis=2)

            preds = loaded_model.predict(twodim,
                                         batch_size=32,
                                         verbose=1)
            for i in range(0, len(preds[0])):
                if i == 0 or i == 1:
                    frag_emotion_dict[0] = frag_emotion_dict[0] + (preds[0][i])
                if i == 2 or i == 3:
                    frag_emotion_dict[1] = frag_emotion_dict[1] + (preds[0][i])
                if i == 4 or i == 5:
                    frag_emotion_dict[2] = frag_emotion_dict[2] + (preds[0][i])
            index = len(group_emotion_dict) + 1
            group_emotion_dict[index] = frag_emotion_dict

        # return all_emotion_dict, bad_val_dict
    # return group_emotion_dict
    return group_emotion_dict

