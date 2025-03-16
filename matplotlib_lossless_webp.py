import matplotlib.pyplot as plt


def patch():
    """Patch matplotlib to force lossless .webp images."""
    original_savefig = plt.Figure.savefig

    def savefig(self, fname, *args, **kwargs):
        if isinstance(fname, str) and fname.lower().endswith('.webp'):
            # just guarding against non-str here to have same error behavior as matplotlib
            kwargs['pil_kwargs'] = {'lossless': True} | kwargs.get('pil_kwargs', {})
            return original_savefig(self, fname, **kwargs)
        return original_savefig(self, fname, *args, **kwargs)

    plt.Figure.savefig = savefig


patch()
