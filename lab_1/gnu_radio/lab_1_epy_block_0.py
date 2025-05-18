import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    """Retificador de meia onda (sinal real)"""

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='Retificador Meia Onda',
            in_sig=[np.float32],
            out_sig=[np.float32]
        )

    def work(self, input_items, output_items):
        # zera os valores negativos
        output_items[0][:] = np.maximum(input_items[0], 0)
        return len(output_items[0])

