history=model.first(
        train_data,
        validation_data=val_data,
epochs=EPOCHS,
callbacks=callbacks
)
plt.plot(history.history['accuracy'],
