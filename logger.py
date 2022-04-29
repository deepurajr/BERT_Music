"""
Code referenced from https://gist.github.com/gyglim/1f8dfb1b5c82627ae3efcfbbadb9f514
"""
import tensorflow as tf
#import torch as tf
from torch.utils.tensorboard import SummaryWriter
import numpy as np
from PIL import Image
from io import BytesIO,StringIO         


class Logger(object):
    
    def __init__(self, log_dir):
        """Create a summary writer logging to log_dir."""
        #self.writer =  tf.compat.v1.summary.FileWriter(log_dir)
        with tf.compat.v1.Session() as sess:
            self.writer = self.writer =  tf.compat.v1.summary.FileWriter(log_dir,  sess.graph)
        #self.writer = SummaryWriter(log_dir=log_dir)

    def scalar_summary(self, tag, value, step):
        """Log a scalar variable."""
        summary =  tf.compat.v1.Summary(value=[tf.compat.v1.Summary.Value(tag=tag, simple_value=value)])
        self.writer.add_summary(summary, step)
        #self.writer.add_scalar(tag, value, step)

    def image_summary(self, tag, images, step):
        """Log a list of images."""

        img_summaries = []
        for i, img in enumerate(images):
            # Write the image to a string
            try:
                s = BytesIO()
            except:
                s = StringIO()
            # scipy.misc.toimage(img).save(s, format="png")
            Image.fromarray(img, mode='L').save(s, "PNG")   
            # Create an Image object
            img_sum = tf.compat.v1.Summary.Image(encoded_image_string=s.getvalue(),
                                       height=img.shape[0],
                                       width=img.shape[1])
            # Create a Summary value
            img_summaries.append( tf.compat.v1.Summary.Value(tag='%s/%d' % (tag, i), image=img_sum))

        # Create and write Summary
        summary =  tf.compat.v1.Summary(value=img_summaries)
        self.writer.add_summary(summary, step)
        #self.writer.add_scalar(tag, img_summaries, step)
        
    def histo_summary(self, tag, values, step, bins=1000):
        """Log a histogram of the tensor of values."""

        # Create a histogram using numpy
        counts, bin_edges = np.histogram(values, bins=bins)

        # Fill the fields of the histogram proto
        hist =  tf.compat.v1.HistogramProto()
        hist.min = float(np.min(values))
        hist.max = float(np.max(values))
        hist.num = int(np.prod(values.shape))
        hist.sum = float(np.sum(values))
        hist.sum_squares = float(np.sum(values**2))

        # Drop the start of the first bin
        bin_edges = bin_edges[1:]

        # Add bin edges and counts
        for edge in bin_edges:
            hist.bucket_limit.append(edge)
        for c in counts:
            hist.bucket.append(c)

        # Create and write Summary
        summary = tf.compat.v1.Summary(value=[tf.compat.v1.Summary.Value(tag=tag, histo=hist)])
        self.writer.add_summary(summary, step)
        #self.writer.add_scalar(tag, hist, step)
        self.writer.flush()