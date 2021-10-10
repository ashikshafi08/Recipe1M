
import tensorflow as tf 
from tensorflow.keras import layers 


# Image Encoder (get the image embeddings)
# Bulding the encodr with tensorflow method at first 

class ImageEncoder(tf.keras.Model):

  def __init__(self , embed_size, shape ,   dropout_rate = 0.5 ,trainable = False , **kwargs):
    super(ImageEncoder , self).__init__(**kwargs)
    
    self.embed_size = embed_size
    self.shape = shape 
    self.dropout_rate = dropout_rate 
    self.trainable = self.trainable

    self.resnet = tf.keras.applications.ResNet50(include_top =False)

  
    self.input_layer = layers.Input(shape = self.shape, name ='image_tensor_input')
    self.project_embed_dense = layers.Dense(embed_size)
    self.dropout = layers.Dropout(rate = self.dropout_rate)
    self.add = layers.Add()
    self.layer_norm = layers.LayerNormalization()


  def call(self , x):

      # Checking if trainable is True 
      if self.trainable is not True:
        for layer in self.resnet.layers:
          layer.trainable = self.trainable 

        
        input = self.input_layer(x)
        preprocess_inp = tf.keras.applications.resnet50(input)
        resnet_embedding = self.resnet(preprocess_inp)

        # Passing the embeddings for projection embeddings 
        projection_embeddings = self.project_embed_dense(resnet_embedding)
        x = tf.nn.gelu(projection_embeddings)
        x = layers.Dense(self.embed_size)
        x = self.dropout(x)

        # Add the projection embedding and the x 
        x = self.add([project_embeddings , x])
        x = self.layer_norm(x)
      return x 
  


    


    
