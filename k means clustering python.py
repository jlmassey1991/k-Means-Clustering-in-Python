# -*- coding: utf-8 -*-
"""

k-means Clustering in Python Adaptation
Created on Mon Feb 17 12:58:48 2025

"""

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "06 K Means Clustering.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNbK0ZvShB20D8oogjHlhcz",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sandipanpaul21/ML-Clustering-in-Python/blob/master/06_K_Means_Clustering.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "MQtVEcs2DsSI"
      },
      "source": [
        "#### **K-Means Clustering**\n",
        "\n",
        "- K Means allows us to define the required number of clusters\n",
        "- Now we first start by taking an arbitrary number of k. Let’s say we take k=3 (k is choosen from **elbow method**)\n",
        "- Algorithm chooses three random points as the centroid \n",
        "- It also computes Euclidean distances from the centroid to all other data points\n",
        "- The algorithm after measuring the distances of all the data points from the centroid associates each data point with a centroid based on its proximity\n",
        "- To measure how good the three clusters are seperated, we use **Silhouette Score**\n",
        "\n",
        "#### **Elbow Method**\n",
        "- In the Elbow method, we are actually varying the number of clusters (K) from 1 – 10. For each value of K, we are calculating WCSS(Within-Cluster Sum of Square)\n",
        "- **WCSS is the sum of squared distance between each point and the centroid in a cluster**\n",
        "- WCSS value is largest when K = 1. \n",
        "\n",
        "####  **Silhouette Score**\n",
        "- Clusters are well apart from each other as the silhouette score is closer to 1\n",
        "- Silhouette Coefficient score is a metric used to calculate the goodness of a clustering technique \n",
        "- Its value ranges from -1 to 1.\n",
        "  1. **Score = 1: Means clusters are well apart** from each other and clearly distinguished.\n",
        "  2. **Score = 0: Means clusters are indifferent**, or we can say that the distance between clusters is not significant.\n",
        "  3. **Score = -1: Means clusters are assigned in the wrong way.**"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qcrOZvxZDrFS",
        "colab": {
          "resources": {
            "http://localhost:8080/nbextensions/google.colab/files.js": {
              "data": "Ly8gQ29weXJpZ2h0IDIwMTcgR29vZ2xlIExMQwovLwovLyBMaWNlbnNlZCB1bmRlciB0aGUgQXBhY2hlIExpY2Vuc2UsIFZlcnNpb24gMi4wICh0aGUgIkxpY2Vuc2UiKTsKLy8geW91IG1heSBub3QgdXNlIHRoaXMgZmlsZSBleGNlcHQgaW4gY29tcGxpYW5jZSB3aXRoIHRoZSBMaWNlbnNlLgovLyBZb3UgbWF5IG9idGFpbiBhIGNvcHkgb2YgdGhlIExpY2Vuc2UgYXQKLy8KLy8gICAgICBodHRwOi8vd3d3LmFwYWNoZS5vcmcvbGljZW5zZXMvTElDRU5TRS0yLjAKLy8KLy8gVW5sZXNzIHJlcXVpcmVkIGJ5IGFwcGxpY2FibGUgbGF3IG9yIGFncmVlZCB0byBpbiB3cml0aW5nLCBzb2Z0d2FyZQovLyBkaXN0cmlidXRlZCB1bmRlciB0aGUgTGljZW5zZSBpcyBkaXN0cmlidXRlZCBvbiBhbiAiQVMgSVMiIEJBU0lTLAovLyBXSVRIT1VUIFdBUlJBTlRJRVMgT1IgQ09ORElUSU9OUyBPRiBBTlkgS0lORCwgZWl0aGVyIGV4cHJlc3Mgb3IgaW1wbGllZC4KLy8gU2VlIHRoZSBMaWNlbnNlIGZvciB0aGUgc3BlY2lmaWMgbGFuZ3VhZ2UgZ292ZXJuaW5nIHBlcm1pc3Npb25zIGFuZAovLyBsaW1pdGF0aW9ucyB1bmRlciB0aGUgTGljZW5zZS4KCi8qKgogKiBAZmlsZW92ZXJ2aWV3IEhlbHBlcnMgZm9yIGdvb2dsZS5jb2xhYiBQeXRob24gbW9kdWxlLgogKi8KKGZ1bmN0aW9uKHNjb3BlKSB7CmZ1bmN0aW9uIHNwYW4odGV4dCwgc3R5bGVBdHRyaWJ1dGVzID0ge30pIHsKICBjb25zdCBlbGVtZW50ID0gZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgnc3BhbicpOwogIGVsZW1lbnQudGV4dENvbnRlbnQgPSB0ZXh0OwogIGZvciAoY29uc3Qga2V5IG9mIE9iamVjdC5rZXlzKHN0eWxlQXR0cmlidXRlcykpIHsKICAgIGVsZW1lbnQuc3R5bGVba2V5XSA9IHN0eWxlQXR0cmlidXRlc1trZXldOwogIH0KICByZXR1cm4gZWxlbWVudDsKfQoKLy8gTWF4IG51bWJlciBvZiBieXRlcyB3aGljaCB3aWxsIGJlIHVwbG9hZGVkIGF0IGEgdGltZS4KY29uc3QgTUFYX1BBWUxPQURfU0laRSA9IDEwMCAqIDEwMjQ7CgpmdW5jdGlvbiBfdXBsb2FkRmlsZXMoaW5wdXRJZCwgb3V0cHV0SWQpIHsKICBjb25zdCBzdGVwcyA9IHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCk7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICAvLyBDYWNoZSBzdGVwcyBvbiB0aGUgb3V0cHV0RWxlbWVudCB0byBtYWtlIGl0IGF2YWlsYWJsZSBmb3IgdGhlIG5leHQgY2FsbAogIC8vIHRvIHVwbG9hZEZpbGVzQ29udGludWUgZnJvbSBQeXRob24uCiAgb3V0cHV0RWxlbWVudC5zdGVwcyA9IHN0ZXBzOwoKICByZXR1cm4gX3VwbG9hZEZpbGVzQ29udGludWUob3V0cHV0SWQpOwp9CgovLyBUaGlzIGlzIHJvdWdobHkgYW4gYXN5bmMgZ2VuZXJhdG9yIChub3Qgc3VwcG9ydGVkIGluIHRoZSBicm93c2VyIHlldCksCi8vIHdoZXJlIHRoZXJlIGFyZSBtdWx0aXBsZSBhc3luY2hyb25vdXMgc3RlcHMgYW5kIHRoZSBQeXRob24gc2lkZSBpcyBnb2luZwovLyB0byBwb2xsIGZvciBjb21wbGV0aW9uIG9mIGVhY2ggc3RlcC4KLy8gVGhpcyB1c2VzIGEgUHJvbWlzZSB0byBibG9jayB0aGUgcHl0aG9uIHNpZGUgb24gY29tcGxldGlvbiBvZiBlYWNoIHN0ZXAsCi8vIHRoZW4gcGFzc2VzIHRoZSByZXN1bHQgb2YgdGhlIHByZXZpb3VzIHN0ZXAgYXMgdGhlIGlucHV0IHRvIHRoZSBuZXh0IHN0ZXAuCmZ1bmN0aW9uIF91cGxvYWRGaWxlc0NvbnRpbnVlKG91dHB1dElkKSB7CiAgY29uc3Qgb3V0cHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKG91dHB1dElkKTsKICBjb25zdCBzdGVwcyA9IG91dHB1dEVsZW1lbnQuc3RlcHM7CgogIGNvbnN0IG5leHQgPSBzdGVwcy5uZXh0KG91dHB1dEVsZW1lbnQubGFzdFByb21pc2VWYWx1ZSk7CiAgcmV0dXJuIFByb21pc2UucmVzb2x2ZShuZXh0LnZhbHVlLnByb21pc2UpLnRoZW4oKHZhbHVlKSA9PiB7CiAgICAvLyBDYWNoZSB0aGUgbGFzdCBwcm9taXNlIHZhbHVlIHRvIG1ha2UgaXQgYXZhaWxhYmxlIHRvIHRoZSBuZXh0CiAgICAvLyBzdGVwIG9mIHRoZSBnZW5lcmF0b3IuCiAgICBvdXRwdXRFbGVtZW50Lmxhc3RQcm9taXNlVmFsdWUgPSB2YWx1ZTsKICAgIHJldHVybiBuZXh0LnZhbHVlLnJlc3BvbnNlOwogIH0pOwp9CgovKioKICogR2VuZXJhdG9yIGZ1bmN0aW9uIHdoaWNoIGlzIGNhbGxlZCBiZXR3ZWVuIGVhY2ggYXN5bmMgc3RlcCBvZiB0aGUgdXBsb2FkCiAqIHByb2Nlc3MuCiAqIEBwYXJhbSB7c3RyaW5nfSBpbnB1dElkIEVsZW1lbnQgSUQgb2YgdGhlIGlucHV0IGZpbGUgcGlja2VyIGVsZW1lbnQuCiAqIEBwYXJhbSB7c3RyaW5nfSBvdXRwdXRJZCBFbGVtZW50IElEIG9mIHRoZSBvdXRwdXQgZGlzcGxheS4KICogQHJldHVybiB7IUl0ZXJhYmxlPCFPYmplY3Q+fSBJdGVyYWJsZSBvZiBuZXh0IHN0ZXBzLgogKi8KZnVuY3Rpb24qIHVwbG9hZEZpbGVzU3RlcChpbnB1dElkLCBvdXRwdXRJZCkgewogIGNvbnN0IGlucHV0RWxlbWVudCA9IGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKGlucHV0SWQpOwogIGlucHV0RWxlbWVudC5kaXNhYmxlZCA9IGZhbHNlOwoKICBjb25zdCBvdXRwdXRFbGVtZW50ID0gZG9jdW1lbnQuZ2V0RWxlbWVudEJ5SWQob3V0cHV0SWQpOwogIG91dHB1dEVsZW1lbnQuaW5uZXJIVE1MID0gJyc7CgogIGNvbnN0IHBpY2tlZFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgaW5wdXRFbGVtZW50LmFkZEV2ZW50TGlzdGVuZXIoJ2NoYW5nZScsIChlKSA9PiB7CiAgICAgIHJlc29sdmUoZS50YXJnZXQuZmlsZXMpOwogICAgfSk7CiAgfSk7CgogIGNvbnN0IGNhbmNlbCA9IGRvY3VtZW50LmNyZWF0ZUVsZW1lbnQoJ2J1dHRvbicpOwogIGlucHV0RWxlbWVudC5wYXJlbnRFbGVtZW50LmFwcGVuZENoaWxkKGNhbmNlbCk7CiAgY2FuY2VsLnRleHRDb250ZW50ID0gJ0NhbmNlbCB1cGxvYWQnOwogIGNvbnN0IGNhbmNlbFByb21pc2UgPSBuZXcgUHJvbWlzZSgocmVzb2x2ZSkgPT4gewogICAgY2FuY2VsLm9uY2xpY2sgPSAoKSA9PiB7CiAgICAgIHJlc29sdmUobnVsbCk7CiAgICB9OwogIH0pOwoKICAvLyBXYWl0IGZvciB0aGUgdXNlciB0byBwaWNrIHRoZSBmaWxlcy4KICBjb25zdCBmaWxlcyA9IHlpZWxkIHsKICAgIHByb21pc2U6IFByb21pc2UucmFjZShbcGlja2VkUHJvbWlzZSwgY2FuY2VsUHJvbWlzZV0pLAogICAgcmVzcG9uc2U6IHsKICAgICAgYWN0aW9uOiAnc3RhcnRpbmcnLAogICAgfQogIH07CgogIGNhbmNlbC5yZW1vdmUoKTsKCiAgLy8gRGlzYWJsZSB0aGUgaW5wdXQgZWxlbWVudCBzaW5jZSBmdXJ0aGVyIHBpY2tzIGFyZSBub3QgYWxsb3dlZC4KICBpbnB1dEVsZW1lbnQuZGlzYWJsZWQgPSB0cnVlOwoKICBpZiAoIWZpbGVzKSB7CiAgICByZXR1cm4gewogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbXBsZXRlJywKICAgICAgfQogICAgfTsKICB9CgogIGZvciAoY29uc3QgZmlsZSBvZiBmaWxlcykgewogICAgY29uc3QgbGkgPSBkb2N1bWVudC5jcmVhdGVFbGVtZW50KCdsaScpOwogICAgbGkuYXBwZW5kKHNwYW4oZmlsZS5uYW1lLCB7Zm9udFdlaWdodDogJ2JvbGQnfSkpOwogICAgbGkuYXBwZW5kKHNwYW4oCiAgICAgICAgYCgke2ZpbGUudHlwZSB8fCAnbi9hJ30pIC0gJHtmaWxlLnNpemV9IGJ5dGVzLCBgICsKICAgICAgICBgbGFzdCBtb2RpZmllZDogJHsKICAgICAgICAgICAgZmlsZS5sYXN0TW9kaWZpZWREYXRlID8gZmlsZS5sYXN0TW9kaWZpZWREYXRlLnRvTG9jYWxlRGF0ZVN0cmluZygpIDoKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgJ24vYSd9IC0gYCkpOwogICAgY29uc3QgcGVyY2VudCA9IHNwYW4oJzAlIGRvbmUnKTsKICAgIGxpLmFwcGVuZENoaWxkKHBlcmNlbnQpOwoKICAgIG91dHB1dEVsZW1lbnQuYXBwZW5kQ2hpbGQobGkpOwoKICAgIGNvbnN0IGZpbGVEYXRhUHJvbWlzZSA9IG5ldyBQcm9taXNlKChyZXNvbHZlKSA9PiB7CiAgICAgIGNvbnN0IHJlYWRlciA9IG5ldyBGaWxlUmVhZGVyKCk7CiAgICAgIHJlYWRlci5vbmxvYWQgPSAoZSkgPT4gewogICAgICAgIHJlc29sdmUoZS50YXJnZXQucmVzdWx0KTsKICAgICAgfTsKICAgICAgcmVhZGVyLnJlYWRBc0FycmF5QnVmZmVyKGZpbGUpOwogICAgfSk7CiAgICAvLyBXYWl0IGZvciB0aGUgZGF0YSB0byBiZSByZWFkeS4KICAgIGxldCBmaWxlRGF0YSA9IHlpZWxkIHsKICAgICAgcHJvbWlzZTogZmlsZURhdGFQcm9taXNlLAogICAgICByZXNwb25zZTogewogICAgICAgIGFjdGlvbjogJ2NvbnRpbnVlJywKICAgICAgfQogICAgfTsKCiAgICAvLyBVc2UgYSBjaHVua2VkIHNlbmRpbmcgdG8gYXZvaWQgbWVzc2FnZSBzaXplIGxpbWl0cy4gU2VlIGIvNjIxMTU2NjAuCiAgICBsZXQgcG9zaXRpb24gPSAwOwogICAgZG8gewogICAgICBjb25zdCBsZW5ndGggPSBNYXRoLm1pbihmaWxlRGF0YS5ieXRlTGVuZ3RoIC0gcG9zaXRpb24sIE1BWF9QQVlMT0FEX1NJWkUpOwogICAgICBjb25zdCBjaHVuayA9IG5ldyBVaW50OEFycmF5KGZpbGVEYXRhLCBwb3NpdGlvbiwgbGVuZ3RoKTsKICAgICAgcG9zaXRpb24gKz0gbGVuZ3RoOwoKICAgICAgY29uc3QgYmFzZTY0ID0gYnRvYShTdHJpbmcuZnJvbUNoYXJDb2RlLmFwcGx5KG51bGwsIGNodW5rKSk7CiAgICAgIHlpZWxkIHsKICAgICAgICByZXNwb25zZTogewogICAgICAgICAgYWN0aW9uOiAnYXBwZW5kJywKICAgICAgICAgIGZpbGU6IGZpbGUubmFtZSwKICAgICAgICAgIGRhdGE6IGJhc2U2NCwKICAgICAgICB9LAogICAgICB9OwoKICAgICAgbGV0IHBlcmNlbnREb25lID0gZmlsZURhdGEuYnl0ZUxlbmd0aCA9PT0gMCA/CiAgICAgICAgICAxMDAgOgogICAgICAgICAgTWF0aC5yb3VuZCgocG9zaXRpb24gLyBmaWxlRGF0YS5ieXRlTGVuZ3RoKSAqIDEwMCk7CiAgICAgIHBlcmNlbnQudGV4dENvbnRlbnQgPSBgJHtwZXJjZW50RG9uZX0lIGRvbmVgOwoKICAgIH0gd2hpbGUgKHBvc2l0aW9uIDwgZmlsZURhdGEuYnl0ZUxlbmd0aCk7CiAgfQoKICAvLyBBbGwgZG9uZS4KICB5aWVsZCB7CiAgICByZXNwb25zZTogewogICAgICBhY3Rpb246ICdjb21wbGV0ZScsCiAgICB9CiAgfTsKfQoKc2NvcGUuZ29vZ2xlID0gc2NvcGUuZ29vZ2xlIHx8IHt9OwpzY29wZS5nb29nbGUuY29sYWIgPSBzY29wZS5nb29nbGUuY29sYWIgfHwge307CnNjb3BlLmdvb2dsZS5jb2xhYi5fZmlsZXMgPSB7CiAgX3VwbG9hZEZpbGVzLAogIF91cGxvYWRGaWxlc0NvbnRpbnVlLAp9Owp9KShzZWxmKTsK",
              "ok": true,
              "headers": [
                [
                  "content-type",
                  "application/javascript"
                ]
              ],
              "status": 200,
              "status_text": ""
            }
          },
          "base_uri": "https://localhost:8080/",
          "height": 76
        },
        "outputId": "93554c48-3d02-4630-94ca-8107d09ff9e1"
      },
      "source": [
        "# Importing Libraries\n",
        "\n",
        "from sklearn import datasets,metrics\n",
        "import matplotlib.pyplot as plt\n",
        "from sklearn.cluster import KMeans\n",
        "from sklearn.datasets import load_iris\n",
        "import numpy as np\n",
        "from sklearn.metrics import silhouette_score\n",
        "import pandas as pd\n",
        "from scipy.spatial import distance # To calculate distances\n",
        "from google.colab import files\n",
        "from IPython.display import Image\n",
        "\n",
        "uploaded = files.upload() # To import image from computer/tab"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-4fe509c2-5729-41e1-9e19-012451a7f974\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-4fe509c2-5729-41e1-9e19-012451a7f974\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script src=\"/nbextensions/google.colab/files.js\"></script> "
            ],
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving 0232A118-EF98-410D-B996-6A0769F9712F.png to 0232A118-EF98-410D-B996-6A0769F9712F.png\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 335
        },
        "id": "szrQVyesRvtF",
        "outputId": "908afc7c-f4ea-4916-da55-c70f2d0ee5c4"
      },
      "source": [
        "print('K Means ALGORITHIM STEPS :')\n",
        "Image('0232A118-EF98-410D-B996-6A0769F9712F.png',height = 300)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "K Means ALGORITHIM STEPS :\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<IPython.core.display.Image object>"
            ]
          },
          "metadata": {
            "image/png": {
              "height": 300
            }
          },
          "execution_count": 23
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 281
        },
        "id": "D7bcZjNXHmcG",
        "outputId": "75da574f-1749-45bc-8ec5-e239d1402142"
      },
      "source": [
        "# Lets take an small example\n",
        "x_axis = np.array([1,2,3,18,19,20])\n",
        "y_axis = np.array([1,2,3,18,19,20])\n",
        "\n",
        "data = pd.DataFrame({'x':x_axis, 'y':y_axis})\n",
        "\n",
        "plt.plot()\n",
        "plt.xlim([0,21])\n",
        "plt.ylim([0,21])\n",
        "plt.title('Dataset')\n",
        "plt.scatter(x_axis,y_axis)\n",
        "plt.show()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4RDtPBJAIew0",
        "outputId": "50e94814-bcf9-414a-c001-6c5572a9a56d"
      },
      "source": [
        "print('For ONE Cluster, all data points should be assigned to 1 Cluster\\n')\n",
        "\n",
        "kmeans = KMeans(n_clusters = 1, max_iter = 100).fit(data)\n",
        "data['clusters'] = kmeans.labels_\n",
        "print('Clusters assigned to each datapoints :')\n",
        "print(data['clusters'])\n",
        "print('\\nSum of Square Error/ WCSS is :',kmeans.inertia_)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "For ONE Cluster, all data points should be assigned to 1 Cluster\n",
            "\n",
            "Clusters assigned to each datapoints :\n",
            "0    0\n",
            "1    0\n",
            "2    0\n",
            "3    0\n",
            "4    0\n",
            "5    0\n",
            "Name: clusters, dtype: int32\n",
            "\n",
            "Sum of Square Error/ WCSS is : 875.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kMeouSnZJ8wE",
        "outputId": "2233dfcc-5059-4dbe-a3e7-10da9db9dddc"
      },
      "source": [
        "print('For TWO Cluster, all data points should be assigned to 2 Clusters\\n')\n",
        "\n",
        "kmeans = KMeans(n_clusters = 2, max_iter = 100).fit(data)\n",
        "data['clusters'] = kmeans.labels_\n",
        "print('Clusters assigned to each datapoints :')\n",
        "print(data['clusters'])\n",
        "print('\\nSum of Square Error/ WCSS is :',kmeans.inertia_)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "For TWO Cluster, all data points should be assigned to 2 Clusters\n",
            "\n",
            "Clusters assigned to each datapoints :\n",
            "0    1\n",
            "1    1\n",
            "2    1\n",
            "3    0\n",
            "4    0\n",
            "5    0\n",
            "Name: clusters, dtype: int32\n",
            "\n",
            "Sum of Square Error/ WCSS is : 8.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Rxs1Gnm8KR0I",
        "outputId": "36c6820f-556c-458b-fb43-b730ab911733"
      },
      "source": [
        "print('For THREE Cluster, all data points should be assigned to 3 Clusters\\n')\n",
        "\n",
        "kmeans = KMeans(n_clusters = 3, max_iter = 100).fit(data)\n",
        "data['clusters'] = kmeans.labels_\n",
        "print('Clusters assigned to each datapoints :')\n",
        "print(data['clusters'])\n",
        "print('\\nSum of Square Error/ WCSS is :',kmeans.inertia_)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "For THREE Cluster, all data points should be assigned to 3 Clusters\n",
            "\n",
            "Clusters assigned to each datapoints :\n",
            "0    1\n",
            "1    1\n",
            "2    1\n",
            "3    0\n",
            "4    2\n",
            "5    2\n",
            "Name: clusters, dtype: int32\n",
            "\n",
            "Sum of Square Error/ WCSS is : 5.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 171
        },
        "id": "bb0qF3AJUXqr",
        "outputId": "25fad1f0-cf89-49c6-e5a1-22af8eb6041e"
      },
      "source": [
        "print('WCSS Formula\\n')\n",
        "print('In K Means, Distance measure is Euclidean Distance Metric')\n",
        "Image('C7423E3E-0827-4D5A-9AF4-85291A8637ED.jpeg')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "WCSS Formula\n",
            "\n",
            "In K Means, Distance measure is Euclidean Distance Metric\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "image/jpeg": "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RWSx3iSIGsy7TrJGFO9SfMjAJKkAoWU96xf+GcNJExkj8V+J0U/8s11NgvLs5P3N2WLEEk5IwM8CmP2B9F+3pUE1zbW+z7RIib2CLuYDcx6KM9SfTrXiGifAPw/oOsN4gtNT1F7108hp5ZhJK0BaRnjLsCSWaXl/vAIgUjbzd8P/AAO8NaBd2J+0T3VnprLLa2swTZHMgGJcoq5ckBmJHLAMeeSB7A//0P78KKKK6DaGyCiiiplsN7BRRRVDCiiigAooooAKKKKACiiigAooooAKKKKACiiigD//2QAA/9sAhAAJBgcQEBAQEBAQFRYRFRAREBYXEBAQERUQEBUVFxcWEhUVGR4oIBgaJxsVFiEyIiUqKy8uLhcfMzgzLDcoLS83AQoKCg0NDhcPDxUtHRUdKystKy0rLTcrLS0tLS0rKy0rLTctNysrNy0tKy0tLS03LS0rLTcrLS0tLSstKy0tLS3/wAARCABsBAADASIAAhEBAxEB/8QAGwABAAIDAQEAAAAAAAAAAAAAAAUGAwQHAQL/xABHEAACAgIBAgQEAgcEBwQLAAABAgADBBESBSEGEzFBFCJRYTKBBxUjQnGRoTNSYtIWJFOCkpTRRFaxwSU0Q1Rjc3SDk7Kz/8QAFgEBAQEAAAAAAAAAAAAAAAAAAAEC/8QAFhEBAQEAAAAAAAAAAAAAAAAAABEB/9oADAMBAAIRAxEAPwDuEREqEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBE0+r9UoxKWvyLAlS65MQSB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nruq/HdMlEWxVNlF6n56RrlojWgRub3QsZcfK6jXXQFvsy7LKj5WgtTYyat3ruhsUqfuTIq7xOeeGMVtYXm2FcxH5ZCjGsF7sVYWC+xn01RJ2G1rsnH2m/4F6bSTdbxcWV5mZ5fLzUC49lh4hVOgUIGx9NkiUWfrHUlxaXvdWZV4jVa8mJZgoAH8WE1undbFuRdivW1d1SV2kEqytXZyCsrKfqpGjr0mXr3UGx6hYtLWDzK0YI3E11swDWn7KO5/h+crfhcj9ZZZxT5uHZj1u15Y2/60GK+Sl52XUJ347IU/TcC6xEQEREBERAREQEREBERAREQEREBERAREQEREBERDJERDRERAREQEREBERAREQPi6oOrI34WBU6JHY+vcdxMeFiJTWlVa8a0UIo2TxUdgBv2meICIiAnmp7EDzUCexARESBERCEREqgiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAmt1DArvUJavJQ6uByZfnQ7U9iPQgH+IE2YgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiIGrfgVPZVcy7sq5cDyYceQ03YHXcdptREDwxPYgIiICNREBERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQP//Z\n",
            "text/plain": [
              "<IPython.core.display.Image object>"
            ]
          },
          "metadata": {},
          "execution_count": 44
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 403
        },
        "id": "8AQi50JHKfH4",
        "outputId": "e5f23e28-2cab-433b-8ae5-169c44ccc5eb"
      },
      "source": [
        "# ELBOW METHOD\n",
        "\n",
        "# How many clusters should we choose ? - Elbow Method\n",
        "# Select the elbow point for number of clusters\n",
        "data = pd.DataFrame({'x':x_axis, 'y':y_axis})\n",
        "\n",
        "sse = {}\n",
        "\n",
        "for k in range(1,6): # Maximum range should be 6, as it contains only 6 data points\n",
        "  kmeans = KMeans(n_clusters=k,max_iter=100).fit(data)\n",
        "  data['clusters'] = kmeans.labels_\n",
        "  sse[k] = kmeans.inertia_\n",
        "  print(\"For cluster = {}, SSE/WCSS is {}\".format(k, sse[k]))\n",
        "\n",
        "plt.figure()\n",
        "plt.plot(list(sse.keys()),list(sse.values()))\n",
        "plt.xlabel(\"Number of Cluster\")\n",
        "plt.ylabel(\"SSE / WCSS\")\n",
        "plt.title(\"ELBOW METHOD\")\n",
        "plt.show()\n",
        "\n",
        "print('Optimum Number of Cluster : 2')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "For cluster = 1, SSE/WCSS is 875.0\n",
            "For cluster = 2, SSE/WCSS is 8.0\n",
            "For cluster = 3, SSE/WCSS is 5.0\n",
            "For cluster = 4, SSE/WCSS is 2.0\n",
            "For cluster = 5, SSE/WCSS is 1.0\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Optimum Number of Cluster : 2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "N5VfcATRWodw"
      },
      "source": [
        "#### **Silhouette Score**\n",
        "- It refers to a method of interpretation and validation of consistency within clusters of data. \n",
        "- The silhouette value is a measure of how similar an object is to its own cluster (cohesion) compared to other clusters (separation). \n",
        "- The silhouette ranges from −1 to +1, where a high value indicates that the object is well matched to its own cluster and poorly matched to neighboring clusters. \n",
        "- If most objects have a high value, then the clustering configuration is appropriate.\n",
        "- If many points have a low or negative value, then the clustering configuration may have too many or too few clusters."
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 353
        },
        "id": "eNxqI7k2Vx8P",
        "outputId": "9eb44cf5-97fa-4474-da3c-8f56ec31c888"
      },
      "source": [
        "print('Silhouette Score Example\\n')\n",
        "Image('F936FB3C-5CD7-4269-93BB-A4C2CEFB75B0.png',height = 300)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Silhouette Score Example\n",
            "\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<IPython.core.display.Image object>"
            ]
          },
          "metadata": {
            "image/png": {
              "height": 300
            }
          },
          "execution_count": 54
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 253
        },
        "id": "-R2cg4j4TCKS",
        "outputId": "93a6b808-4bed-46fb-8b67-4fd2f7658c20"
      },
      "source": [
        "print('Elbow Method VS Silhouette Score \\n')\n",
        "Image('404FF6A7-9BC8-4DB7-921B-5986E1EA8E99.png',height = 200)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Elbow Method VS Silhouette Score \n",
            "\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<IPython.core.display.Image object>"
            ]
          },
          "metadata": {
            "image/png": {
              "height": 200
            }
          },
          "execution_count": 52
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mL9ZySvtNiok",
        "outputId": "dad1d36b-7504-4726-d44c-9304a30c8345"
      },
      "source": [
        "# Silhouette Score\n",
        "\n",
        "data = pd.DataFrame({'x':x_axis, 'y':y_axis})\n",
        "\n",
        "for n_clusters in range(0,6):# Maximum range should be 6, as it contains only 6 data points\n",
        "  kmeans = KMeans(n_clusters=k,max_iter=100).fit(data)\n",
        "  label = kmeans.labels_\n",
        "  sil_coeff = silhouette_score(data,label,metric = 'euclidean')\n",
        "  print('For cluster= {}, Silhouette Coefficient is {}'.format(n_clusters,sil_coeff))\n",
        "\n",
        "print('\\n It is same for every cluster, so choose from Elbow Method')"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "For cluster= 0, Silhouette Coefficient is 0.08333333333333333\n",
            "For cluster= 1, Silhouette Coefficient is 0.08333333333333333\n",
            "For cluster= 2, Silhouette Coefficient is 0.08333333333333333\n",
            "For cluster= 3, Silhouette Coefficient is 0.08333333333333333\n",
            "For cluster= 4, Silhouette Coefficient is 0.08333333333333333\n",
            "For cluster= 5, Silhouette Coefficient is 0.08333333333333333\n",
            "\n",
            " It is same for every cluster, so choose from Elbow Method\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IgadKpnrSlNM",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 204
        },
        "outputId": "7724149c-1b35-4a72-c449-ad8d524a3229"
      },
      "source": [
        "# Lets Take another Dataset : IRIS Dataset\n",
        "# Loading the Dataset\n",
        "\n",
        "iris = datasets.load_iris()\n",
        "iris_data = pd.DataFrame(iris.data)\n",
        "iris_data.columns = iris.feature_names\n",
        "iris_data['Type']=iris.target\n",
        "iris_data.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>sepal length (cm)</th>\n",
              "      <th>sepal width (cm)</th>\n",
              "      <th>petal length (cm)</th>\n",
              "      <th>petal width (cm)</th>\n",
              "      <th>Type</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>5.1</td>\n",
              "      <td>3.5</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>4.9</td>\n",
              "      <td>3.0</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>4.7</td>\n",
              "      <td>3.2</td>\n",
              "      <td>1.3</td>\n",
              "      <td>0.2</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4.6</td>\n",
              "      <td>3.1</td>\n",
              "      <td>1.5</td>\n",
              "      <td>0.2</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5.0</td>\n",
              "      <td>3.6</td>\n",
              "      <td>1.4</td>\n",
              "      <td>0.2</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "   sepal length (cm)  sepal width (cm)  ...  petal width (cm)  Type\n",
              "0                5.1               3.5  ...               0.2     0\n",
              "1                4.9               3.0  ...               0.2     0\n",
              "2                4.7               3.2  ...               0.2     0\n",
              "3                4.6               3.1  ...               0.2     0\n",
              "4                5.0               3.6  ...               0.2     0\n",
              "\n",
              "[5 rows x 5 columns]"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YYotNIqgS1PM",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e0004c97-ca28-45c2-9833-f782f0332a80"
      },
      "source": [
        "# Preparing Data\n",
        "# Here we have the target variable ‘Type’. \n",
        "# We need to remove the target variable, used to work in an unsupervised learning \n",
        "# The iloc function is used to get the features we require. \n",
        "# We also use .values function to get an array of the dataset. \n",
        "# Note : We transformed the dataset to an array so that we can plot the graphs of the clusters\n",
        "\n",
        "iris_X = iris_data.iloc[:, [0, 1, 2,3]].values\n",
        "print(iris_X[:5,:]) # Printing First 5 Rows"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[5.1 3.5 1.4 0.2]\n",
            " [4.9 3.  1.4 0.2]\n",
            " [4.7 3.2 1.3 0.2]\n",
            " [4.6 3.1 1.5 0.2]\n",
            " [5.  3.6 1.4 0.2]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nQQGS8_dTvbU",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d18fde86-40a3-4f64-f212-49f7d5a56924"
      },
      "source": [
        "# Now we will separate the target variable from the original dataset \n",
        "# And again convert it to an array by using numpy\n",
        "iris_Y = iris_data['Type']\n",
        "iris_Y = np.array(iris_Y)\n",
        "print(iris_Y)\n",
        "# Frequency count of the Output clusters\n",
        "unique, counts = np.unique(iris_Y, return_counts=True)\n",
        "freq_1 = dict(zip(unique, counts))\n",
        "freq_1"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n",
            " 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n",
            " 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2\n",
            " 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2\n",
            " 2 2]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{0: 50, 1: 50, 2: 50}"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7zdlBmMrilBn",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1e0a64f1-553e-4710-9cf6-4ce747c80c34"
      },
      "source": [
        "# Filtering Setosa\n",
        "\n",
        "Setosa = iris_data['Type'] == 0\n",
        "print(\"Filtering Setosa, True means its Setosa and False means Non Setosa\")\n",
        "print(Setosa.head())\n",
        "print(\"Top 6 Rows of Setosa\")\n",
        "Setosa_v2 = iris_data[Setosa]\n",
        "print(Setosa_v2[Setosa_v2.columns[0:2]].head())\n",
        "print(\"Last 6 Rows of Setosa\")\n",
        "print(Setosa_v2[Setosa_v2.columns[0:2]].tail())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Filtering Setosa, True means its Setosa and False means Non Setosa\n",
            "0    True\n",
            "1    True\n",
            "2    True\n",
            "3    True\n",
            "4    True\n",
            "Name: Type, dtype: bool\n",
            "Top 6 Rows of Setosa\n",
            "   sepal length (cm)  sepal width (cm)\n",
            "0                5.1               3.5\n",
            "1                4.9               3.0\n",
            "2                4.7               3.2\n",
            "3                4.6               3.1\n",
            "4                5.0               3.6\n",
            "Last 6 Rows of Setosa\n",
            "    sepal length (cm)  sepal width (cm)\n",
            "45                4.8               3.0\n",
            "46                5.1               3.8\n",
            "47                4.6               3.2\n",
            "48                5.3               3.7\n",
            "49                5.0               3.3\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_wOmXWLJWzq5",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 485
        },
        "outputId": "bd62ae06-73d3-4085-84dd-a445023bcce6"
      },
      "source": [
        "# Filtering Setosa for 2D Plot \n",
        "\n",
        "print(\"Setosa for 2D Plot\")\n",
        "print(\"X Axis points\")\n",
        "print(iris_X[iris_Y == 0,0])\n",
        "print(\"Y Axis Points\")\n",
        "print(iris_X[iris_Y == 0,1])\n",
        "print('\\n')\n",
        "# For Setosa in Target Column i.e, iris_Y = 0 \n",
        "# In other word it should range from (0,0) to (0,1)\n",
        "plt.scatter(iris_X[iris_Y == 0, 0], iris_X[iris_Y == 0, 1], \n",
        "            s = 80, c = 'orange', label = 'Iris-setosa')\n",
        "plt.xlim([4.5,8])\n",
        "plt.ylim([2,4.5])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Setosa for 2D Plot\n",
            "X Axis points\n",
            "[5.1 4.9 4.7 4.6 5.  5.4 4.6 5.  4.4 4.9 5.4 4.8 4.8 4.3 5.8 5.7 5.4 5.1\n",
            " 5.7 5.1 5.4 5.1 4.6 5.1 4.8 5.  5.  5.2 5.2 4.7 4.8 5.4 5.2 5.5 4.9 5.\n",
            " 5.5 4.9 4.4 5.1 5.  4.5 4.4 5.  5.1 4.8 5.1 4.6 5.3 5. ]\n",
            "Y Axis Points\n",
            "[3.5 3.  3.2 3.1 3.6 3.9 3.4 3.4 2.9 3.1 3.7 3.4 3.  3.  4.  4.4 3.9 3.5\n",
            " 3.8 3.8 3.4 3.7 3.6 3.3 3.4 3.  3.4 3.5 3.4 3.2 3.1 3.4 4.1 4.2 3.1 3.2\n",
            " 3.5 3.6 3.  3.4 3.5 2.3 3.2 3.5 3.8 3.  3.8 3.2 3.7 3.3]\n",
            "\n",
            "\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(2.0, 4.5)"
            ]
          },
          "metadata": {},
          "execution_count": 12
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXwAAAD8CAYAAAB0IB+mAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAYl0lEQVR4nO3dfZBldXng8e/TPSPzAuKuTjEDMwQqhBB5EWUkuqSsWVhZEWosVqokVbKSNTsxFSKmUmUkpThhqVKzW4m7sSrWBGoX1PiyE7DQiIEqYI1bFZYeJDAOrEGXOMPw0oLCjD1gz/Szf5zbTnvp7nu6+9x7zu3z/VR13dv3/Pp3nnuq6+nT5/6e80RmIkla/kbqDkCSNBgmfElqCRO+JLWECV+SWsKEL0ktYcKXpJYonfAjYjQivhMRX59l29URMR4RD3W+frvaMCVJS7ViAWOvBR4FXj3H9i9n5jVLD0mS1A+lzvAjYiNwKXBTf8ORJPVL2TP8TwMfBo6bZ8y7I+JtwPeAP8jMvd0DImIbsA1g7dq1551xxhkLDFeS2m3Xrl0/ysx1i/nZngk/Ii4Dns3MXRGxZY5hXwO+mJkvR8TvALcAF3YPyswdwA6AzZs359jY2GJilqTWioh/XuzPlrmkcwGwNSKeAL4EXBgRn585IDOfy8yXO9/eBJy32IAkSf3RM+Fn5nWZuTEzTwGuBO7JzPfOHBMRG2Z8u5Xiw11JUoMsZJXOL4iIG4CxzLwD+GBEbAUOA88DV1cTnhpt8gDsvR1eehpWrYdNl8PK+T7mkVSnqOv2yF7DH2KZsOeTsPs/QYzCkZdgdBXkETjrY/D6j0BE3VFKy1JE7MrMzYv52UWf4avF9nwSdt8IRw4dfe3wweJx943F45nXDT4uSfPy1gpamMkDxZn9kYnZtx+ZKJL+5MHBxiWpJxO+Fmbv7cVlnPnECOy7fTDxSCrNhK+Feenp4pr9fI68BIeeGkw8kkoz4WthVq0vPqCdz+gqWL1h/jGSBs6Er4XZdHmxGmc+OQUbLx9MPJJKM+FrYVYeVyy9HF0z+/bRNXDWR2HlsYONS1JPLsvUwr3+I8XjrOvwP3p0u6RGMeFr4SKKdfanXwP7vlp8QLt6Q3EZxzN7qbFM+Fq8lcfBqVfVHYWkkryGL0ktYcKXpJYw4UtSS5jwJaklTPiS1BKu0mkbm5ZIrWXCb4u5mpY88AGblkgtYcJvC5uWSK3nNfw2sGmJJEz47WDTEkmY8NvBpiWSMOG3g01LJGHCbweblkjChN8ONi2RhMsy6zXIIiiblkitF5lZy443b96cY2Njtey7dnMVQeWR/hdBTR6waYk0xCJiV2ZuXszPeoZfhzqLoGxaIrWW1/AHzSIoSTUx4Q+aRVCSamLCHzSLoCTVxIQ/aBZBSaqJCX/QLIKSVBMT/qBZBCWpJi7LrEPbiqDssiU1goVXdVruRVB1FphJy9RACq8iYhQYA57MzMu6th0D3AqcBzwHvCczn1hMQK2y3Iug7LIlNcpCruFfCzw6x7b3Az/OzNOAPwc+tdTANOQsMJMap1TCj4iNwKXATXMMeRdwS+f5TuCiCP9XbzULzKTGKXuG/2ngw8DUHNtPAvYCZOZh4AXgtd2DImJbRIxFxNj4+PgiwtXQsMBMapyeCT8iLgOezcxdS91ZZu7IzM2ZuXndunVLnU5NZoGZ1DhlzvAvALZGxBPAl4ALI+LzXWOeBDYBRMQK4HiKD2/VVhaYSY3TM+Fn5nWZuTEzTwGuBO7JzPd2DbsDeF/n+RWdMfWs91QzWGAmNc6iC68i4gZgLDPvAG4GPhcRjwPPU/xh0CBN7IdHtsPEPlizEc7eDmtOrDemthWYSQ1n4dWwm5qC+y6Bp+965bb1F8OWO2Gk5jtoLPcCM2mA7HjVZnMleyhev+8SuPDvBhtTt+VeYCYNCW+eNswm9s+d7Kc9fRccenow8UhqNBP+MHtke7XjJC1rJvxhNrGv3Lif/rC/cUgaCib8YbZmY7lxa0/ubxyShoIJf5idvb3acZKWNVfp9MsL34MHthUfmK5eD2/eAcefXu0+1pxYLL2c74Pb9RcX++8HG5tIQ8V1+FU7cgT+9gw4+Pgrtx17Glz6GIz2uIvkQtSxDt/GJlJtXIffJHMleyhe/9szYOs/Vbe/kZFinf3Efth9Q/EB7dqTi8s4/Tqzt7GJNJRM+FV64XtzJ/tpBx+HA9+H43652n2vORHO/2y1c87m541NDs2+fbqxyem/bzWt1DB+aFulB7aVG3f/f+xvHP1kYxNpaJnwq1S2ovXQ/v7G0U82NpGGlgm/SmWvma+u+S6WS2FjE2lomfCr9OYd5cb9+l/1N45+srGJNLRM+FU6/vRi6eV8jj2t+g9sB8nGJtLQcpVO1S59rPc6/IUqU+A0yCIoG5tIQ8mEX7WREfjl/wAP/wnkJDAFjECsLF5fSBHUXAVOD3zgaIET9B5TdRFURLHO/vRrbGwiDRETftWmi5Ly5RkvThXfL7QoqUyB0/TzOoqgbGwiDRVvrVClyQNw2wlzFyVBcY373z3T+0y41Fyri/8CpuZZJll2f5KGwlJureCHtlWqsiipzFyZQI8/2BZBSerwkk6VqixKKjPX1M96z2MRlKQOz/CrVGVRUpm5Rl4FIyur2Z+kZc+EX6Uqi5LKzBUB9FiBYxGUpA4TfpWqLEoqNdfH4OzrLYKSVEpzr+EPuptS2f31GldlUdJC5rIISlIPzVuWOehuSmX3t9C4Jg9UV5RUZq4q9yepsZayLLN5Cf+7n+gUEk28ctv0JYoqC4nK7m/QcUnSLJbPOvyfd1OaJanC0W5KkwcHu79DTw02Lknqg2Yl/EF3Uyq7v4e32+VJ0tBrVsIfdDelsvub2GuXJ0lDr1kJf9DdlMrub80muzxJGnrNSviD7qZUdn/nbLfLk6Sh16yEP+huSmX3t3rDwuOa2A/3b4N731k8TszSuHzyAPzgVtjzp8Xj5IGlv6de6tinpEZo3rLMpq7DP3Kkdyer0VGYmoL7LoGn73rluPUXw5Y7i/kG+R4X8j4lNVpf1+FHxCrgW8AxFJW5OzPz411jrgb+M/Bk56XPZOZN883b8374gy4k6rW/e/7t7El82vqL4cK/KzfuhC2DX9NvHYG0LPQ74QewNjMPRsRK4NvAtZn5DzPGXA1szsxryu54qBqgTOyHr57Ue9w7vgPffGPvcaOr5l/1U3XTkiobs0iqVV8Lr7IwXVG0svNVz3Wgujyyvdy4//2b5cZNHZ5/e9Vr+gdd3yCpkUp9aBsRoxHxEPAscHdm3j/LsHdHxMMRsTMiNs0xz7aIGIuIsfHx8SWEPWAT+8qNe/lH5cb1WvFT9Zr+Qdc3SGqkUgk/M49k5rnARuD8iDira8jXgFMy8xzgbuCWOebZkZmbM3PzunXrlhL3YK3ZWG7cMa8rN67X2XbVa/oHXd8gqZEWtCwzM38C3Au8o+v15zLz5c63NwHnVRNeQ5y9vdy4C75YbtxIj7tSV72mf9D1DZIaqWfCj4h1EfGazvPVwNuBx7rGzDw13Ao8WmWQtVtzYrG6Zj7rL4Z/eW65cWcNuGnJoOsbJDVSmQYoG4BbImKU4g/EVzLz6xFxAzCWmXcAH4yIrcBh4Hng6iVHVmUDlIn9xQevE/uKyzNnby+S+EJsubP3+vqy46bXuz9yA5AwNdnpTRuLb1rS6z1W2ZhF0lDqmfAz82HgFWsNM/P6Gc+vA6pZxD1XgdADH1h4gdBcRVDf/6ujyXek4mLjiGKd/fi3itU4eaR4HyMritdnxj7dWGXm9wtV9j1GFOvsT7/GRilSSzWv0rbKAqGyxVJVzlUmfmjme5TUeMun41WVBUJli6UufwpWr69mrsv+Ce48p0f8q4uz+qkKCq+qfI+ShsLy6XhVZYFQ2WKpMuPKzvV/tvWOP5OedWt1vEdJy16ZD20Hp8oCobLFUj/9YXVzHdrfO/6pn/Wep473KGnZa9YZfpUFQmWLpdaeXN1cq0/sHf/IqzorcuZRx3uUtOw1K+FXWSBUtliqzLiyc52/o3f8EUCP1Th1vEdJy16zEn6VBUJli6XKfJhZdq5Xn1Yi/o/B2RUVXlX5HiUte81K+FCssz/ro8VqlhXHQqwoHkdXL7xAaMudcyfEmcVSVc41M/6RVcBI8Tgz/qa+R0nLWrM+tIVqC4RGRoo16BP7YfcNxYeXa08uLnEs9Kx3IQVV0LUaJ39xYU5T36OkZa1Z6/CbrGxBmJ2lJPXR8lmH31STB4pbPcyWxKF4ffeNxZl6mXGTB2ffLkl9ZMIvo2xB2MPb7SwlqbFM+GWULQib2GtnKUmNZcIvo2xB2JpNdpaS1Fgm/DLKFoSds93OUpIaq7kJf/IA/OBW2POnxePkgVeOmdgP92+De99ZPE7s708sZQvCVm+ws5SkxmreOvwyDVAyB9/Y5Nf+CJ65b/Z7z6/7jWI72FlKUmM1L+Hv+WRnHfuMe8of7ixj3H1j8ThX4oXi9fsuqb7px6OfgvFvz75t/NvF9jOvs7OUpMZqVuFVqQYoq+ffPq3Kph9VNmaRpCVYPoVXZda7T02Wm6vKph9VNmaRpJo0K+GXWe/eaxXMtCqbflTZmEWSatKshF9mvXuvM+1pVTb9qLIxiyTVpFkJv8x6917doqZV2fSjysYsklSTZiX8UuvdPzb4ph9VNmaRpJo0b1nmzHXsmUXT75FXFcsdp9ex/9ofzb4OH2Zv+jF5oPjg9aWni8szmy4vkvhME/uLD3on9hW9Ys/eXnSUmi0u19dLGkLNS/jT5msgUrbpR5VFXK6vlzTkmrUOH6ptIFJmrvmKuKBI+lUXcUnSIi1lHX6zEn6VBU5l5hpZBVM9lltCtUVckrQE7Sq8KlvgVGausmv6qyzikqSaNCvhV1ngVKqI63C5uKos4pKkmjQr4VdZ4FSqiKvkZ9ZVFnFJUk2alfCrLHAqM1fZqt0qi7gkqSbNSvhVFjiVmevs6wdfxCVJNWneOvwqC5ymxz5yQ/Hzebi4jBOj/S3ikqQGal7Cr7LAKbNYZz9z6WVOFl/P3Fck+wg4YQs887+AI8UfhhgFRovXI47O1auIa3qsJDVQz4QfEauAbwHHdMbvzMyPd405BrgVOA94DnhPZj6xpMhWHgenXrWkKeY8c4ejnbFO2FIUZ+XLR7flYeDw0Q5bZ15XrhNX2YIwSapBmWv4LwMXZuYbgHOBd0TEW7rGvB/4cWaeBvw58Klqw1yEif3zV9BCsf3hP5m9EheK13ffCBNPFWf2vcZNHlxazJLURz0TfhamM9nKzld3ee67gFs6z3cCF0XUfH2jdLFUr5U8I7B7ux2vJA29Uqt0ImI0Ih4CngXuzsz7u4acBOwFyMzDwAvAa2eZZ1tEjEXE2Pj4+NIi72ViX7lxvZZuHnkJfrrXjleShl6phJ+ZRzLzXGAjcH5EnLWYnWXmjszcnJmb161bt5gpyluzsdy4Xmfuo6tg7SY7Xkkaegtah5+ZPwHuBd7RtelJYBNARKwAjqf48LY+pYulet1vZwrO2m7HK0lDr2fCj4h1EfGazvPVwNuBx7qG3QG8r/P8CuCerOs2nNPWnFiuqOqcj/cu9FqzwY5XkoZemXX4G4BbImKU4g/EVzLz6xFxAzCWmXcANwOfi4jHgeeBK/sW8UJsubN3UdX0Z8u9Cr3seCVpyDXrfvj90qszFhQVtGUKvcqOk6Q+WD4NUCRJ81o+DVAkSX1jwpekljDhS1JLmPAlqSVM+JLUEiZ8SWoJE74ktYQJX5JawoQvSS1hwpekljDhS1JLmPAlqSVM+JLUEiZ8SWoJE74ktYQJX5JawoQvSS1hwpekljDhS1JLmPAlqSVM+JLUEiZ8SWoJE74ktYQJX5JawoQvSS1hwpekljDhS1JLmPAlqSVM+JLUEiZ8SWoJE74ktYQJX5JawoQvSS3RM+FHxKaIuDci9kTEdyPi2lnGbImIFyLioc7X9f0JV5K0WCtKjDkM/GFmPhgRxwG7IuLuzNzTNe7vM/Oy6kOUJFWh5xl+Zj6VmQ92nh8AHgVO6ndgkqRqLegafkScArwRuH+WzW+NiH+MiDsj4sw5fn5bRIxFxNj4+PiCg5UkLV7phB8RxwJ/A3woM1/s2vwg8EuZ+QbgL4CvzjZHZu7IzM2ZuXndunWLjVmStAilEn5ErKRI9l/IzNu6t2fmi5l5sPP8G8DKiHhdpZFKkpakzCqdAG4GHs3MP5tjzPrOOCLi/M68z1UZqCRpacqs0rkAuAp4JCIe6rz2x8DJAJn5WeAK4Hcj4jBwCLgyM7MP8UqSFqlnws/MbwPRY8xngM9UFZQkqXpW2kpSS5jwJaklTPiS1BImfElqCRO+JLWECV+SWsKEL0ktUV/Cf+lp+MGtMHmgthAkqU3qS/gTT8LY78FtJ8B3PwEW5kpSX5W5tUL/HD5YPO6+sXg887r6YpGkZa4Z1/CPTBRJf/Jg3ZFI0rLVjIQPECOw7/a6o5CkZas5Cf/IS3DoqbqjkKRlqzkJf3QVrN5QdxSStGw1J+HnFGy8vO4oJGnZakbCH10DZ30UVh5bdySStGzVuyxzxbGQR4pk//qP1BqKJC139SX8NSfBmz9RXMbxzF6S+q6+hL9qPZx6VW27l6S2acY1fElS35nwJaklTPiS1BImfElqCRO+JLWECV+SWsKEL0ktYcKXpJYw4UtSS5jwJaklTPiS1BImfElqCRO+JLWECV+SWsKEL0ktYcKXpJbomfAjYlNE3BsReyLiuxFx7SxjIiL+W0Q8HhEPR8Sb+hOuJGmxynS8Ogz8YWY+GBHHAbsi4u7M3DNjzCXAr3S+fh34y86jJKkhep7hZ+ZTmflg5/kB4FHgpK5h7wJuzcI/AK+JiA2VRytJWrQF9bSNiFOANwL3d206Cdg74/t9ndee6vr5bcC2zrcvR8Tuhey/YV4H/KjuIJbA+Os1zPEPc+ww/PH/6mJ/sHTCj4hjgb8BPpSZLy5mZ5m5A9jRmW8sMzcvZp4mMP56GX99hjl2WB7xL/ZnS63SiYiVFMn+C5l52yxDngQ2zfh+Y+c1SVJDlFmlE8DNwKOZ+WdzDLsD+Ped1TpvAV7IzKfmGCtJqkGZSzoXAFcBj0TEQ53X/hg4GSAzPwt8A3gn8DgwAfxWiXl3LDjaZjH+ehl/fYY5dmhx/JGZVQYiSWooK20lqSVM+JLUEgNJ+BExGhHfiYivz7Lt6ogYj4iHOl+/PYiYyoqIJyLikU5sr1gO1fTbSpSIf0tEvDDj+F9fR5yziYjXRMTOiHgsIh6NiLd2bW/6se8Vf5OP/a/OiOuhiHgxIj7UNaaxx79k/I09/gAR8Qed29nsjogvRsSqru3HRMSXO8f//k6d1LwWVHi1BNdSVOi+eo7tX87MawYUy2L868ycq1BjGG4rMV/8AH+fmZcNLJry/ivwzcy8IiJeBazp2t70Y98rfmjosc/M/wucC8UJG8Uy69u7hjX2+JeMHxp6/CPiJOCDwOsz81BEfAW4EvgfM4a9H/hxZp4WEVcCnwLeM9+8fT/Dj4iNwKXATf3eV028rUQfRMTxwNsolgSTmT/LzJ90DWvssS8Z/7C4CPh+Zv5z1+uNPf5d5oq/6VYAqyNiBcXJwv6u7e8Cbuk83wlc1FlGP6dBXNL5NPBhYGqeMe/u/Eu4MyI2zTOuDgncFRG7OreG6DbXbSWaolf8AG+NiH+MiDsj4sxBBjePU4Fx4L93LgfeFBFru8Y0+diXiR+aeey7XQl8cZbXm3z8Z5orfmjo8c/MJ4H/AvyQ4hY1L2TmXV3Dfn78M/Mw8ALw2vnm7WvCj4jLgGczc9c8w74GnJKZ5wB3c/QvVlP8Rma+ieLf19+LiLfVHdAC9Yr/QeCXMvMNwF8AXx10gHNYAbwJ+MvMfCPwU+Aj9Ya0IGXib+qx/7nOpaitwP+sO5bF6BF/Y49/RPwLijP4U4ETgbUR8d6lztvvM/wLgK0R8QTwJeDCiPj8zAGZ+Vxmvtz59ibgvD7HtCCdv7Rk5rMU1wDP7xrS6NtK9Io/M1/MzIOd598AVkbE6wYe6CvtA/Zl5vSN+nZSJNCZmnzse8bf4GM/0yXAg5n5zCzbmnz8p80Zf8OP/78B/l9mjmfmJHAb8K+6xvz8+Hcu+xwPPDffpH1N+Jl5XWZuzMxTKP6tuiczf+GvVNc1v60UH+42QkSsjaIHAJ1/xy8Guu/w2djbSpSJPyLWT1/3i4jzKX4n5v2lGYTMfBrYGxHTdwa8CNjTNayxx75M/E099l1+k7kvhzT2+M8wZ/wNP/4/BN4SEWs6MV7EK3PjHcD7Os+voMiv81bSDmqVzi+IiBuAscy8A/hgRGylaLTyPHB1HTHN4QTg9s7vxArgrzPzmxHxAVjSbSUGpUz8VwC/GxGHgUPAlb1+aQbo94EvdP4t/wHwW0N07KF3/E0+9tMnCW8HfmfGa0Nz/EvE39jjn5n3R8ROistOh4HvADu6cufNwOci4nGK3Hllr3m9tYIktYSVtpLUEiZ8SWoJE74ktYQJX5JawoQvSS1hwpekljDhS1JL/H+YYLEiB83EeAAAAABJRU5ErkJggg==\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "vN6l86eLnvni",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "20fdffca-6431-4a4c-bd38-acc90ff57ea6"
      },
      "source": [
        "# Filtering Versicolour\n",
        "\n",
        "Versi = iris_data['Type'] == 1\n",
        "print(\"Filtering Versicolour, True means its Versicolour and False means Non Versicolour\")\n",
        "print(Versi.head())\n",
        "print(\"Top 6 Rows of Versicolour\")\n",
        "Versi_v2 = iris_data[Versi]\n",
        "print(Versi_v2[Versi_v2.columns[0:2]].head())\n",
        "print(\"Last 6 Rows of Versicolour\")\n",
        "print(Versi_v2[Versi_v2.columns[0:2]].tail())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Filtering Versicolour, True means its Versicolour and False means Non Versicolour\n",
            "0    False\n",
            "1    False\n",
            "2    False\n",
            "3    False\n",
            "4    False\n",
            "Name: Type, dtype: bool\n",
            "Top 6 Rows of Versicolour\n",
            "    sepal length (cm)  sepal width (cm)\n",
            "50                7.0               3.2\n",
            "51                6.4               3.2\n",
            "52                6.9               3.1\n",
            "53                5.5               2.3\n",
            "54                6.5               2.8\n",
            "Last 6 Rows of Versicolour\n",
            "    sepal length (cm)  sepal width (cm)\n",
            "95                5.7               3.0\n",
            "96                5.7               2.9\n",
            "97                6.2               2.9\n",
            "98                5.1               2.5\n",
            "99                5.7               2.8\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "M7mb70sXnTMg",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 485
        },
        "outputId": "e0807975-b90a-4608-ec2c-237590445439"
      },
      "source": [
        "# Filtering Versicolour for 2D Plot \n",
        "\n",
        "print(\"Versicolour for 2D Plot\")\n",
        "print(\"X Axis points\")\n",
        "print(iris_X[iris_Y == 1,0])\n",
        "print(\"Y Axis Points\")\n",
        "print(iris_X[iris_Y == 1,1])\n",
        "print('\\n')\n",
        "plt.scatter(iris_X[iris_Y == 1, 0], iris_X[iris_Y == 1, 1], \n",
        "            s = 80, c = 'yellow', label = 'Iris-versicolour')\n",
        "\n",
        "plt.xlim([4.5,8])\n",
        "plt.ylim([2,4.5])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Versicolour for 2D Plot\n",
            "X Axis points\n",
            "[7.  6.4 6.9 5.5 6.5 5.7 6.3 4.9 6.6 5.2 5.  5.9 6.  6.1 5.6 6.7 5.6 5.8\n",
            " 6.2 5.6 5.9 6.1 6.3 6.1 6.4 6.6 6.8 6.7 6.  5.7 5.5 5.5 5.8 6.  5.4 6.\n",
            " 6.7 6.3 5.6 5.5 5.5 6.1 5.8 5.  5.6 5.7 5.7 6.2 5.1 5.7]\n",
            "Y Axis Points\n",
            "[3.2 3.2 3.1 2.3 2.8 2.8 3.3 2.4 2.9 2.7 2.  3.  2.2 2.9 2.9 3.1 3.  2.7\n",
            " 2.2 2.5 3.2 2.8 2.5 2.8 2.9 3.  2.8 3.  2.9 2.6 2.4 2.4 2.7 2.7 3.  3.4\n",
            " 3.1 2.3 3.  2.5 2.6 3.  2.6 2.3 2.7 3.  2.9 2.9 2.5 2.8]\n",
            "\n",
            "\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(2.0, 4.5)"
            ]
          },
          "metadata": {},
          "execution_count": 14
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qD2TL0cwocaN",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "8f0f6856-4922-4750-c195-7b8a5e9b4fa5"
      },
      "source": [
        "# Filtering Virginica\n",
        "\n",
        "Virginica = iris_data['Type'] == 2\n",
        "print(\"Filtering Virginica, True means its Virginica and False means Non Virginica\")\n",
        "print(Virginica.head())\n",
        "print(\"Top 6 Rows of Virginica\")\n",
        "Virginica_v2 = iris_data[Virginica]\n",
        "print(Virginica_v2[Virginica_v2.columns[0:2]].head())\n",
        "print(\"Last 6 Rows of Virginica\")\n",
        "print(Virginica_v2[Virginica_v2.columns[0:2]].tail())"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Filtering Virginica, True means its Virginica and False means Non Virginica\n",
            "0    False\n",
            "1    False\n",
            "2    False\n",
            "3    False\n",
            "4    False\n",
            "Name: Type, dtype: bool\n",
            "Top 6 Rows of Virginica\n",
            "     sepal length (cm)  sepal width (cm)\n",
            "100                6.3               3.3\n",
            "101                5.8               2.7\n",
            "102                7.1               3.0\n",
            "103                6.3               2.9\n",
            "104                6.5               3.0\n",
            "Last 6 Rows of Virginica\n",
            "     sepal length (cm)  sepal width (cm)\n",
            "145                6.7               3.0\n",
            "146                6.3               2.5\n",
            "147                6.5               3.0\n",
            "148                6.2               3.4\n",
            "149                5.9               3.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wsnoGdx0objs",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 485
        },
        "outputId": "32980a65-ea59-4287-d1cf-95f3b53396ff"
      },
      "source": [
        "# Filtering Virginica for 2D Plot\n",
        "\n",
        "print(\"Virginica for 2D Plot\")\n",
        "print(\"X Axis points\")\n",
        "print(iris_X[iris_Y == 2,0])\n",
        "print(\"Y Axis Points\")\n",
        "print(iris_X[iris_Y == 2,1])\n",
        "print('\\n')\n",
        "plt.scatter(iris_X[iris_Y == 2, 0], iris_X[iris_Y == 2, 1], \n",
        "            s = 80, c = 'green', label = 'Iris-virginica')\n",
        "plt.xlim([4.5,8])\n",
        "plt.ylim([2,4.5])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Virginica for 2D Plot\n",
            "X Axis points\n",
            "[6.3 5.8 7.1 6.3 6.5 7.6 4.9 7.3 6.7 7.2 6.5 6.4 6.8 5.7 5.8 6.4 6.5 7.7\n",
            " 7.7 6.  6.9 5.6 7.7 6.3 6.7 7.2 6.2 6.1 6.4 7.2 7.4 7.9 6.4 6.3 6.1 7.7\n",
            " 6.3 6.4 6.  6.9 6.7 6.9 5.8 6.8 6.7 6.7 6.3 6.5 6.2 5.9]\n",
            "Y Axis Points\n",
            "[3.3 2.7 3.  2.9 3.  3.  2.5 2.9 2.5 3.6 3.2 2.7 3.  2.5 2.8 3.2 3.  3.8\n",
            " 2.6 2.2 3.2 2.8 2.8 2.7 3.3 3.2 2.8 3.  2.8 3.  2.8 3.8 2.8 2.8 2.6 3.\n",
            " 3.4 3.1 3.  3.1 3.1 3.1 2.7 3.2 3.3 3.  2.5 3.  3.4 3. ]\n",
            "\n",
            "\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(2.0, 4.5)"
            ]
          },
          "metadata": {},
          "execution_count": 16
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HCShLm9HUWHn",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 286
        },
        "outputId": "43d5e2ea-c320-451c-9ca0-71e76384bfb1"
      },
      "source": [
        "# Visualise Classes all at once\n",
        "\n",
        "# In this Iris dataset, we have three classes (0,1,2)\n",
        "# We visualise these classes in a 2-D graph \n",
        "# This will help us in comparing the original classes with the clusters created \n",
        "# Plot the three type of flowers on a graph\n",
        "\n",
        "plt.scatter(iris_X[iris_Y == 0, 0], iris_X[iris_Y == 0, 1], \n",
        "            s = 80, c = 'orange', label = 'Iris-setosa')\n",
        "plt.scatter(iris_X[iris_Y == 1, 0], iris_X[iris_Y == 1, 1], \n",
        "            s = 80, c = 'yellow', label = 'Iris-versicolour')\n",
        "plt.scatter(iris_X[iris_Y == 2, 0], iris_X[iris_Y == 2, 1], \n",
        "            s = 80, c = 'green', label = 'Iris-virginica')\n",
        "plt.legend()\n",
        "\n",
        "# Inference : \n",
        "# We find that we have three classes with two types of Iris flowers overlapping each other"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.legend.Legend at 0x7f19f4e46e50>"
            ]
          },
          "metadata": {},
          "execution_count": 17
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXUAAAD7CAYAAACVMATUAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjIsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+WH4yJAAAgAElEQVR4nO2df3RU1bn3PzvJQBIm+JNFiAGRRgQNCArYCgLq2yBKqemtS1tr5e0rkSpXW2sFbsGbIrcgulrbXluLdnmLpdaW23AtStUqPwRvWQINiiSXIkWkCUjlVibmh0lmv3+cGQjJzDk7mTNnzsw8H1bWJHN29nnOnuHJmXO+z/dRWmsEQRCEzCAn1QEIgiAI7iFJXRAEIYOQpC4IgpBBSFIXBEHIICSpC4IgZBCS1AVBEDII46SulMpVSv1ZKbU+xrY5SqljSqnayNcd7oYpCIIgmJDXi7H3AnXAwDjbn9Naz088JEEQBKGvGCV1pVQpcAPwb8B9buz43HPP1cOHD3djKkEQhKxh586df9daD4q33fRM/THgAaDIZsw/KaWmAvuAb2qt37ebcPjw4ezYscNw94IgCAKAUuo9u+2O19SVUrOAD7TWO22G/R4YrrUeC7wC/CLOXFVKqR1KqR3Hjh1z2rUgCILQS0xulE4GZiulDgK/Bq5RSv2y6wCt9Yda67bIj08Bl8eaSGu9Sms9QWs9YdCguJ8eBEEQhD7imNS11ou01qVa6+HALcBrWuuvdB2jlBrS5cfZWDdUBUEQBI/pjfrlNJRSS4EdWuvngXuUUrOBDuA4MMed8ISsoT0E79dA6xHIL4ahlRCwu4Uj9Ib29nYOHz5Ma2trqkMRDMnPz6e0tJRAINCr31Opst6dMGGClhulAlrD3hWw5yFQudDZCrn5oDuhfAlcvBCUSnWUac9f//pXioqKOOecc1Cynr5Ha82HH35IKBTiggsuOG2bUmqn1npCvN+VilIhtexdAXuWQWcLdDSB7rAeO1us5/euSHWEGUFra6sk9DRCKcU555zTp09WktSF1NEess7QO5tjb+9sthJ7e5O3cWUoktDTi76+XpLUhdTxfo11ycUOlQOHa7yJRxAyAEnqQupoPWJdQ7ejsxVaGr2JRzhFewgOrIa9K63H9lDCUwaDwbjbrrzyyoTnj8f3vve9pM3tRySpC6kjv9i6KWpHbj4UDLEfI7iH1vDOcvjdYNhxN+z+jvX4u8HW8y4LKzo6OgB44403XJ23K5LUBcErhlZaKhc7dBhKK72JR/DkxvWmTZu46qqrmD17NhdffDFw6iy+sbGRqVOnMm7cOMrLy3n99dd7/P4777zDpEmTGDduHGPHjuUvf/kLAL/85S9PPn/nnXfS2dnJwoULaWlpYdy4cdx6660AfP/736e8vJzy8nIee+wxAD7++GNuuOEGLr30UsrLy3nuuecAWLp0KRMnTqS8vJyqqipSpRbsDZLUhdQRKLJki7mFsbfnFkL5YgjE/9guuIiHN6537drFD3/4Q/bt23fa87/61a+YMWMGtbW17N69m3HjxvX43SeeeIJ7772X2tpaduzYQWlpKXV1dTz33HNs27aN2tpacnNzWbNmDStWrKCgoIDa2lrWrFnDzp07efrpp9m+fTt/+tOfePLJJ/nzn//MH/7wB0pKSti9ezd79uzhuuuuA2D+/Pm8+eab7Nmzh5aWFtav7+E87jskqQup5eKFVuLOLYC8IKg86zG3wHr+4oWpjjB78PDG9aRJk3rorwEmTpzI008/TXV1NW+//TZFRT0L0D7zmc/wve99j4cffpj33nuPgoICXn31VXbu3MnEiRMZN24cr776KgcOHOjxu1u3bqWyspIBAwYQDAb5whe+wOuvv86YMWN45ZVXWLBgAa+//jpnnHEGABs3buSKK65gzJgxvPbaa7zzzjsJH3uy6XNFqSC4glJwySIYOR8Or7NuihYMsS65yBm6t3h443rAgAExn586dSpbtmzhhRdeYM6cOdx3330UFRXx3e9+F4CnnnqKL3/5y1xxxRW88MILXH/99fzsZz9Da83tt9/O8uXL+xTPyJEj2bVrFy+++CKLFy/m2muv5YEHHuCuu+5ix44dDB06lOrq6rSoyJUzdcEfBIrggtvg4gesR0no3uODG9fvvfcegwcPZu7cudxxxx3s2rWLyspKamtrqa2tZcKECRw4cIARI0Zwzz338PnPf5633nqLa6+9lrVr1/LBBx8AcPz4cd57z3KoDQQCtLe3A3DVVVexbt06mpub+fjjj6mpqeGqq66ioaGBwsJCvvKVr/Dtb3+bXbt2nUzg5557Lk1NTaxduzZpx+0mcqYuCILF0Ep4c579mCTfuN60aROPPPIIgUCAYDDI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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "q3vCVatczYBY",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 493
        },
        "outputId": "eb1fa4ab-cd98-4761-911d-3d1ebdf2656e"
      },
      "source": [
        "# K Means\n",
        "\n",
        "# Deciding Value of K\n",
        "# The most crucial aspect of K-Means clustering is deciding the value of K\n",
        "# We do this by performing Elbow Analysis \n",
        "\n",
        "wcss=[]\n",
        "for i in range(1, 11):\n",
        "    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300,\n",
        "                    n_init = 10, random_state = 0)\n",
        "    kmeans.fit(iris_X)\n",
        "    wcss.append(kmeans.inertia_)\n",
        "    sse[i] = kmeans.inertia_\n",
        "    print(\"For cluster = {}, SSE/WCSS is {}\".format(i, sse[i]))\n",
        "\n",
        "plt.plot(range(1, 11), wcss)\n",
        "plt.title('The elbow method')\n",
        "plt.xlabel('Number of clusters')\n",
        "plt.ylabel('WCSS')\n",
        "\n",
        "# Inference : \n",
        "# Cluster 1 means only one cluster, inshort variance of the dataset\n",
        "# Variance in Cluster 1 = 681\n",
        "# Cluster 2 means two cluster i.e, Variance in Cluster 2 = 152\n",
        "# Same way for Variance in Cluster 3 = 78\n",
        "# Vairance in Cluster is also knows as Within Cluster Sum of Square (WCSS)\n",
        "# Normally as we increase number of clusters, within Sum of Square will decrease \n",
        "\n",
        "# In the elbow graph, we look for the points where the drop falls and the line smoothens out\n",
        "# In the above graph, this happens for k=3. \n",
        "# Another way of understanding this is that we note the point at which the WCSS is less \n",
        "# and try to find the number of clusters for our dataset. \n",
        "# We see that at the number of clusters = 3, WCSS is less than 100, which is good for us. \n",
        "# So we take k =3.\n",
        "# We will check Silhouette Coefficient also for 3 and 4 Clusters respectively"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "For cluster = 1, SSE/WCSS is 681.3706\n",
            "For cluster = 2, SSE/WCSS is 152.34795176035792\n",
            "For cluster = 3, SSE/WCSS is 78.85144142614601\n",
            "For cluster = 4, SSE/WCSS is 57.25600931571815\n",
            "For cluster = 5, SSE/WCSS is 46.44618205128205\n",
            "For cluster = 6, SSE/WCSS is 39.03998724608725\n",
            "For cluster = 7, SSE/WCSS is 34.299712121212124\n",
            "For cluster = 8, SSE/WCSS is 30.014398496240602\n",
            "For cluster = 9, SSE/WCSS is 28.036906353450473\n",
            "For cluster = 10, SSE/WCSS is 26.53452922077922\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Text(0, 0.5, 'WCSS')"
            ]
          },
          "metadata": {},
          "execution_count": 18
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "lTHnXGs90GGq",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "72f5ccd2-66ba-4fb0-dec2-36433e59f3d5"
      },
      "source": [
        "# Running K-Means Model\n",
        "\n",
        "# We now run K-Means clustering for obtaining a 3 cluster solution.\n",
        "cluster_Kmeans = KMeans(n_clusters=3)\n",
        "model_kmeans = cluster_Kmeans.fit(iris_X)\n",
        "pred_kmeans = model_kmeans.labels_\n",
        "print(pred_kmeans)\n",
        "\n",
        "# Frequency count of the Output clusters\n",
        "unique, counts = np.unique(pred_kmeans, return_counts=True)\n",
        "dict(zip(unique, counts))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1\n",
            " 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0\n",
            " 0 0 0 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 0 2 2 2 2 0 2 2 2 2\n",
            " 2 2 0 0 2 2 2 2 0 2 0 2 0 2 2 0 0 2 2 2 2 2 0 2 2 2 2 0 2 2 2 0 2 2 2 0 2\n",
            " 2 0]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "{0: 62, 1: 50, 2: 38}"
            ]
          },
          "metadata": {},
          "execution_count": 19
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mezxq4Fx030O",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 376
        },
        "outputId": "747d6323-513a-4487-a049-4944d69a4df4"
      },
      "source": [
        "# Visualizing Output\n",
        "\n",
        "print('Original Cluster Frequency',freq_1)\n",
        "# Frequency count of the Output clusters\n",
        "unique, counts = np.unique(pred_kmeans, return_counts=True)\n",
        "print('K Means Output Cluster Frequency',dict(zip(unique, counts)))\n",
        "# Silhouette Score\n",
        "print('Silhouette Score for 3 Clusters',silhouette_score(iris_X,pred_kmeans))\n",
        "print(\"\\n\")\n",
        "\n",
        "# In the above output we got value labels: ‘0’, ‘1’  and ‘2’\n",
        "# For a better understanding, we can visualize these clusters.\n",
        "\n",
        "plt.scatter(iris_X[pred_kmeans == 0, 0], iris_X[pred_kmeans == 0, 1], \n",
        "            s = 80, c = 'orange', label = 'Iris-setosa')\n",
        "plt.scatter(iris_X[pred_kmeans == 1, 0], iris_X[pred_kmeans == 1, 1], \n",
        "            s = 80, c = 'yellow', label = 'Iris-versicolour')\n",
        "plt.scatter(iris_X[pred_kmeans == 2, 0], iris_X[pred_kmeans == 2, 1], \n",
        "            s = 80, c = 'green', label = 'Iris-virginica')\n",
        "plt.legend()\n",
        "\n",
        "# Inference : \n",
        "# When compared to the original classes we find that the observations of the class label \n",
        "# \"1\" has been correctly formed into a separate well-defined cluster\n",
        "# however, for the other two classes, clusters are not as correct. \n",
        "# This is mainly because, in the original dataset, these two class labels were overlapping each other \n",
        "# which makes it difficult for the clustering algorithm as it works best for clear neat separate observations. \n",
        "# Still, the clusters have been formed, more or less correctly\n",
        "# Silhouette Score = 0.55 which is not bad enough (should be tend to 1)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Original Cluster Frequency {0: 50, 1: 50, 2: 50}\n",
            "K Means Output Cluster Frequency {0: 62, 1: 50, 2: 38}\n",
            "Silhouette Score for 3 Clusters 0.5528190123564091\n",
            "\n",
            "\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<matplotlib.legend.Legend at 0x7f19eac99810>"
            ]
          },
          "metadata": {},
          "execution_count": 20
        },
        {
          "output_type": "display_data",
          "data": {
            "image/png": "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\n",
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ]
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jXNotcalLWmu",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "27286acf-2166-4513-d0d2-f3f5df405e15"
      },
      "source": [
        "# If we take 4 Cluster to Check Silhouetter Score\n",
        "cluster_Kmeans = KMeans(n_clusters=4)\n",
        "model_kmeans = cluster_Kmeans.fit(iris_X)\n",
        "labels_1 = model_kmeans.labels_\n",
        "print(\"Silhouette Score for 4 Cluster\")\n",
        "print(silhouette_score(iris_X,labels_1))\n",
        "print('\\n')\n",
        "\n",
        "# Inference : \n",
        "# As we can observe Score is 0.49 (decrease so reject 4 Cluster)\n",
        "# Optimal number of cluster=3 as its silhouette score is greater than that of 4 clusters\n",
        "wcss = []\n",
        "\n",
        "for k in range(2,20):\n",
        "  kmeans = KMeans(n_clusters= k,max_iter=100).fit(iris_X)\n",
        "  label = kmeans.labels_\n",
        "  sil_coeff = silhouette_score(iris_X,label,metric = 'euclidean')\n",
        "  print('For cluster= {}, Silhouette Coefficient is {}'.format(k,sil_coeff))"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Silhouette Score for 4 Cluster\n",
            "0.4980505049972867\n",
            "\n",
            "\n",
            "For cluster= 2, Silhouette Coefficient is 0.681046169211746\n",
            "For cluster= 3, Silhouette Coefficient is 0.5528190123564091\n",
            "For cluster= 4, Silhouette Coefficient is 0.4980505049972867\n",
            "For cluster= 5, Silhouette Coefficient is 0.4887488870931048\n",
            "For cluster= 6, Silhouette Coefficient is 0.3664804028900824\n",
            "For cluster= 7, Silhouette Coefficient is 0.3566882476581684\n",
            "For cluster= 8, Silhouette Coefficient is 0.3598224057544486\n",
            "For cluster= 9, Silhouette Coefficient is 0.3311879738342126\n",
            "For cluster= 10, Silhouette Coefficient is 0.31176492992430954\n",
            "For cluster= 11, Silhouette Coefficient is 0.3239524663368962\n",
            "For cluster= 12, Silhouette Coefficient is 0.30692302322609377\n",
            "For cluster= 13, Silhouette Coefficient is 0.3011211881105722\n",
            "For cluster= 14, Silhouette Coefficient is 0.2808283122551038\n",
            "For cluster= 15, Silhouette Coefficient is 0.29543493729805287\n",
            "For cluster= 16, Silhouette Coefficient is 0.3089537581524615\n",
            "For cluster= 17, Silhouette Coefficient is 0.2961051290749642\n",
            "For cluster= 18, Silhouette Coefficient is 0.29436627821638256\n",
            "For cluster= 19, Silhouette Coefficient is 0.27720782666683685\n"
          ]
        }
      ]
    }
  ]
}
