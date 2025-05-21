<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
def train_model():
train_data, val_data,test_data=
load_data(train_DIR,VAL_DIR, TEST_DIR)
model=
create_model1(input_shape=(IMG_SIZE[0],
                         IMG_SIZE[1],3),
              num_classes=train_data.num_classes)

 HEAD
 test
callbacks=[
modelcheckpoint(MODEL_PATH,
                       save_best_only=true),
       Earlystopping(patience=5,
 HEAD
                     restore_best_weight=true)
 test

                     restore_best_weight=true
                     )
 test
history=model.first(
train_data,
validation_data=val_data,
epochs=EPOCHS,


callbacks=callbacks)
plt.plot(history.history['accuracy'],


plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()
plt.title('training accuracy')
plt savefig('training_accuracy.png')
plt.close()
print("training complete.model HEAD
      saved to:",MODEL_PATH)
<<<<<<< HEAD
>>>>>>> first
=======

<<<<<<< HEAD
>>>>>>> test
=======

 saved to:",MODEL_PATH)
 second
>>>>>>> test
