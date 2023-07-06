## Learning to Synthesize a 4D RGBD Light Field from a Single Image (re-implementation)

[Pratul P. Srinivasan](https://people.eecs.berkeley.edu/~pratul/), [Tongzhou Wang](https://ssnl.github.io/), Ashwin Sreelal, [Ravi Ramamoorthi](http://cseweb.ucsd.edu/~ravir/), [Ren Ng](http://www.eecs.berkeley.edu/Faculty/Homepages/yirenng.html/)

In the International Conference on Computer Vision (ICCV) 2017 (Spotlight Oral Presentation)
## Original Link
[Github](https://github.com/pratulsrinivasan/Local_Light_Field_Synthesis)

[Paper](https://arxiv.org/abs/1708.03292)

## Dependencies
- tensorflow
- tensorflow_addons
- pillow

## Contents

This repository contains:
1) **Local_Light_Field_Synthesis.ipynb** Jupyter notebook with training code of the algorithm. 
1) **validation.ipynb** Jupyter notebook with validation code of the algorithm. 
1) **checkpoints** Pretrained model (training on Flowers Dataset)


## Results 
Example Input 2D Image

![Example Input 2D Image](https://people.eecs.berkeley.edu/~pratul/lf_synthesis/central.png)

Synthesized 4D Light Field

![Synthesized 4D Light Field](https://people.eecs.berkeley.edu/~pratul/lf_synthesis/pred.gif)

Synthesized Synthetic Depth-of-Field (Focused on Flower)

![Synthesized Synthetic Depth-of-Field](https://people.eecs.berkeley.edu/~pratul/lf_synthesis/full.png)


Synthesized Synthetic Depth-of-Field (Focused on Background)

![Synthesized Synthetic Depth-of-Field](https://people.eecs.berkeley.edu/~pratul/lf_synthesis/full2.png)
