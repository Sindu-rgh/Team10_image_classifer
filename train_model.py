def train_model():
train_data, val_data,test_data=
load_data(train_DIR,VAL_DIR, TEST_DIR)
model=
create_model1(input_shape=(IMG_SIZE[0],
                         IMG_SIZE[1],3),
              num_classes=train_data.num_classes)
