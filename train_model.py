plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend()
plt.title('training accuracy')
plt savefig('training_accuracy.png')
plt.close()
print("training complete.model
 saved to:",MODEL_PATH)
