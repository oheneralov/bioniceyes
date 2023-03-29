import React, { useState } from 'react';
import { RNCamera } from 'react-native-camera';
import Icon from 'react-native-vector-icons/dist/FontAwesome';
import { TouchableOpacity, Alert, StyleSheet, SafeAreaView, Button, View, Text } from 'react-native';

const PendingView = () => (
    <View
        style={{
            flex: 1,
            backgroundColor: 'lightgreen',
            justifyContent: 'center',
            alignItems: 'center',
        }}
    >
        <Text>Waiting</Text>
    </View>
);

export default function Camera() {

    let camera = null;
    const [takingPic, setPicState] = useState(false);


    takePicture = async () => {
        if (camera && !takingPic) {
            camera.resumePreview();

            let options = {
                quality: 0.85,
                fixOrientation: true,
                forceUpOrientation: true,
            };

            setPicState(true);

            try {
                const data = await camera.takePictureAsync(options);
                Alert.alert('Success', JSON.stringify(data));
            } catch (err) {
                Alert.alert('Error', 'Failed to take picture: ' + (err.message || err));
                return;
            } finally {
                setPicState(false);
            }
        }
    };


    return (
        <SafeAreaView style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
            <RNCamera
                ref={ref => {
                    camera = ref;
                }}

                style={{ flex: 1 }}
                type={RNCamera.Constants.Type.back}
                androidCameraPermissionOptions={{
                    title: 'Permission to use camera',
                    message: 'We need your permission to use your camera',
                    buttonPositive: 'Ok',
                    buttonNegative: 'Cancel',
                }} >
                <View >
                    <TouchableOpacity>
                        <Text style={{ fontSize: 14 }}> SNAP </Text>
                    </TouchableOpacity>
                </View>
            </RNCamera>

            <Button
                style={styles.btnAlignment}
                title="Take photo"
                color="#841584"
                onPress={takePicture} />
        </SafeAreaView>
    );
}


const styles = StyleSheet.create({
    btnAlignment: {
        flex: 1,
        flexDirection: 'column',
        justifyContent: 'flex-end',
        alignItems: 'center',
        marginBottom: 20,
    },
});