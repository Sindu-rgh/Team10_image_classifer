def train_model():
    train_data, val_daata,test_data=
    load_data(train_DIR, VAL_DIR, TEST_DIR)
    model=
create_model(input_shape=(IMG_SIZE[0],
                          IMG_SIZE[1], 3),
             num_classes=train_data.num_classes)

callbacks=[
        modelcheckpoint(MODEL_PATH,
                        save_best_only=true),
        EarlyStopping(patience=5,
                      restore_best_weight=true)
        ]
history=model.fit(
        train_data,
        validation_data=val_data,
        epochs=EPOCHS,
        callbacks=callbacks
        )
plt.plot(history.history['accuracy'],
         label='train accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt
