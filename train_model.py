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
plt.title('training accuracy')
plt savefig('training_accuracy.png')
plt.close()
print("training complete.model
      saved to:",MODEL_PATH)
#======== 4. PREDICT SINGLE IMAGE
========
def predict_image(img_path):
    model=load_model(MODEL_PATH)
    img=load_img(img_path,
                 targeted_size=IMG_SIZE)
    img_array=img_to_array(img)/
    255.0
    img_array=
    np.expand_dims(img_array,axis=0)
    prediction=
    model.predict(img_array)
    predicted_class=
    np.argmax(prediction) 
    print(f"predicted class index:
    {predicted_class}")
    return predicted_class
def evaluate_model():

