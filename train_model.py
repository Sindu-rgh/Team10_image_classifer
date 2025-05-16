callbacks=[
       modelcheckpoint(MODEL_PATH,
                       save_best_only=true),
       Earlystopping(patience=5,
