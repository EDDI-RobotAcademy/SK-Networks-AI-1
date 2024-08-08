import numpy as np

from convolution_neural_network.repository.cnn_repository_impl import ConvolutionNeuralNetworkRepositoryImpl
from convolution_neural_network.service.cnn_service import ConvolutionNeuralNetworkService


class ConvolutionNeuralNetworkServiceImpl(ConvolutionNeuralNetworkService):

    # cifar10 데이터셋
    # https://www.cs.toronto.edu/~kriz/cifar.html
    # 고양이가 3 개가 5
    # 기타 (비행기 0, 자동차 1, 새 2, 사슴 4, 개구리 6, 말 7, 배 8, 트럭 9)

    TARGET_CIFAR10_CLASSES = [3, 5]
    CIFAR10_INPUT_SHAPE = (32, 32, 3)

    targetClassName = ['고양이', '개']

    def __init__(self):
        self.convolutionNeuralNetworkRepositoryImpl = ConvolutionNeuralNetworkRepositoryImpl()

    def imageTrain(self):
        print("service -> imageTrain()")


        # 이건 그냥 불러온거
        (trainImageList, trainLabelList), (testImageList, testLabelList) = (
            self.convolutionNeuralNetworkRepositoryImpl.loadCifar10Data())


        # 이건 필터링을 하기 위한 작업
        trainImageList, trainLabelList = self.convolutionNeuralNetworkRepositoryImpl.filteringClasses(
            trainImageList, trainLabelList, self.TARGET_CIFAR10_CLASSES
        )

        testImageList, testLabelList = self.convolutionNeuralNetworkRepositoryImpl.filteringClasses(
            testImageList, testLabelList, self.TARGET_CIFAR10_CLASSES
        )

        # numpy형식(arr)으로 있을 것이기 때문에 float형식(소수점을 표현하기 위해)으로 변환
        trainImageList = trainImageList.astype('float32')
        testImageList = testImageList.astype('float32')

        # Generator하는 이유 = 데이터의 안정성을 높이기 위해 -> 무슨 말인지는 레포인플을 가서 확인해보면 알 것이다. 미래의 나야.
        trainGenerator, testGenerator = (
            self.convolutionNeuralNetworkRepositoryImpl.createDataGenerator(
                trainImageList, trainLabelList, testImageList, testLabelList
            ))

        numberOfClass = len(self.TARGET_CIFAR10_CLASSES)
        model = self.convolutionNeuralNetworkRepositoryImpl.createModel(
                                    self.CIFAR10_INPUT_SHAPE, numberOfClass)



        compiledModel = self.convolutionNeuralNetworkRepositoryImpl.modelCompile(model)
        fittedModel = self.convolutionNeuralNetworkRepositoryImpl.fitModel(
                                    compiledModel, trainGenerator, testGenerator)

        fittedModel.save('cnn_model.h5')



    def imagePredict(self, file):
        print("service -> imagePredict()")

        image = self.convolutionNeuralNetworkRepositoryImpl.readImageFile(file)
        print("service -> imagePredict(): after readImageFile()")

        loadedModel = self.convolutionNeuralNetworkRepositoryImpl.loadModel('cnn_model.h5')
        print("service -> imagePredict(): after loadModel()")

        prediction = self.convolutionNeuralNetworkRepositoryImpl.predict(image, loadedModel)
        print(f"prediction: {prediction}")