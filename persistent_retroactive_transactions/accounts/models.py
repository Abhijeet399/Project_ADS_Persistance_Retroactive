from django.db import models
import pickle  # To serialize the queue object

class Account(models.Model):
    name = models.CharField(max_length=100, unique=True)
    queue_data = models.BinaryField()  # Stores serialized queue object
    version = models.IntegerField(default=0)

    def set_queue(self, queue_obj):
        """Serialize and store queue object."""
        self.queue_data = pickle.dumps(queue_obj)
    
    def get_queue(self):
        """Deserialize and retrieve queue object."""
        return pickle.loads(self.queue_data)
