{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "90526750-ca01-4d7e-aa9f-aa7a0c05d6ed",
   "metadata": {},
   "source": [
    "### 3. Custom Loss Function \n",
    "Implement a custom loss function in TensorFlow/Keras. Explain the purpose of the loss \n",
    "function and provide an example scenario where it would be useful."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "82e2fa0d-5fb7-469e-8bde-ccdf56e7311e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import tensorflow as tf\n",
    "from tensorflow.keras import backend as K\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a8e5fd95-9512-43f7-9e7e-f2a2562f36c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def weighted_mse(y_true, y_pred, weights):\n",
    "    \"\"\"\n",
    "    Custom weighted mean squared error loss function.\n",
    "    \n",
    "    Parameters:\n",
    "    y_true -- true labels\n",
    "    y_pred -- predicted labels\n",
    "    weights -- weights for each sample in the batch\n",
    "    \n",
    "    Returns:\n",
    "    Weighted MSE loss value\n",
    "    \"\"\"\n",
    "    # Compute the squared differences between true and predicted labels\n",
    "    squared_diff = tf.square(y_true - y_pred)\n",
    "    # Multiply the squared differences by the weights\n",
    "    weighted_squared_diff = squared_diff * weights\n",
    "    # Return the mean of the weighted squared differences\n",
    "    return K.mean(weighted_squared_diff, axis=-1)\n",
    "\n",
    "# Usage in a model\n",
    "# Assume `weights` is a tensor of shape (batch_size,)\n",
    "weights = tf.constant([1.0, 2.0, 0.5, 1.5]) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3b5c905c-7706-4d55-a79c-5382684095b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\GANGA GHOSH\\anaconda3\\Lib\\site-packages\\keras\\src\\layers\\core\\dense.py:87: UserWarning: Do not pass an `input_shape`/`input_dim` argument to a layer. When using Sequential models, prefer using an `Input(shape)` object as the first layer in the model instead.\n",
      "  super().__init__(activity_regularizer=activity_regularizer, **kwargs)\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/10\n",
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m1s\u001b[0m 1s/step - loss: 0.7240\n",
      "Epoch 2/10\n",
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 74ms/step - loss: 0.6527\n",
      "Epoch 3/10\n",
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 58ms/step - loss: 0.5859\n",
      "Epoch 4/10\n",
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 63ms/step - loss: 0.5233\n",
      "Epoch 5/10\n",
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 50ms/step - loss: 0.4649\n",
      "Epoch 6/10\n",
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 48ms/step - loss: 0.4109\n",
      "Epoch 7/10\n",
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 47ms/step - loss: 0.3609\n",
      "Epoch 8/10\n",
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 45ms/step - loss: 0.3155\n",
      "Epoch 9/10\n",
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 42ms/step - loss: 0.2741\n",
      "Epoch 10/10\n",
      "\u001b[1m1/1\u001b[0m \u001b[32m━━━━━━━━━━━━━━━━━━━━\u001b[0m\u001b[37m\u001b[0m \u001b[1m0s\u001b[0m 46ms/step - loss: 0.2367\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<keras.src.callbacks.history.History at 0x23e346a49e0>"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "# Create a model\n",
    "model = tf.keras.models.Sequential([\n",
    "    tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),\n",
    "    tf.keras.layers.Dense(1)\n",
    "])\n",
    "\n",
    "# Compile the model with the custom loss function\n",
    "model.compile(optimizer='adam', loss=lambda y_true, y_pred: weighted_mse(y_true, y_pred, weights))\n",
    "\n",
    "X_train = np.random.rand(4, 10)\n",
    "y_train = np.random.rand(4, 1)\n",
    "\n",
    "# Train the model\n",
    "model.fit(X_train, y_train, epochs=10)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9f199fac-c27c-4fde-b7e7-5f3741d5e12f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
