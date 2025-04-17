def train_model():
    train_data, val_daata,test_data=
    load_data(train_DIR, VAL_DIR, TEST_DIR)
    model=
    create_model(input_shape=(IMG_SIZE[0],
    IMG_SIZE[1], 3),
    NUM_Classes=train_data.num_classes)
    
    call backs = [
            modelcheckpoint(MODEL_PATH,
                            save_best_only=True),
            EarlyStopping(patience=5,
                          restore_best_weights=True)
            ]
    history=model.fit(
            train_data,
            validation_data=val_data,
            epochs=EPOCHS,
            callbacks=callbacks
            )
    plt.plot(history.history['accuracy'],
             label='train accuracy')

    plt.plot(history.history['val_accuracy'],

             label='validation accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('accuracy')
    plt.legend()
