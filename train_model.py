 HEAD
callbacks=[
modelcheckpoint(MODEL_PATH,
                       save_best_only=true),
       Earlystopping(patience=5,
                     restore_best_weight=true
                     )
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


 saved to:",MODEL_PATH)
 second
