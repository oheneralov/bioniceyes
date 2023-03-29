/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 */

import * as React from 'react';
import { Text, View, TextInput, StyleSheet, SafeAreaView} from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { SetStateAction } from 'react';
import {RNCamera} from 'react-native-camera';
import Camera from './components/Camera'

function HomeScreen() {
  let camera = null;

  return (
    <SafeAreaView style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
    <Camera/>
    </SafeAreaView>
  );
}

function AboutScreen() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text style={styles.about}>This goal of this project is:{"\n"}
    1. to create bionic eyes. Bionic eyes will be an electronic appliance which can function on the basis of the artificial intelligence.{"\n"} 
    Since blind people cannot see, the artificial intelligence can see instead of them and pass signals to a brain {"\n"}
    via person's sensors about the surrounding objects. {"\n"}
    In future we plan to use the following workflow: An images is converted to signals and are transmitted to skin and ear receptors {"\n"}
    to pass signals to a brain.{"\n"}
    2. create a device (artificial finger with AI) which reads text and voice it. It will be a helper for a blind person.{"\n"}
    3. create a smartphone application which will provide audio hints about a current location of a blind person. For example, "shop", "school" etc.{"\n"}
    4. Create ultrasonic glasses which play sound when there is something in the front of a person</Text>
    </View>
  );
}

function SettingsScreen() {
  const [volume, setVolume] = React.useState('10');

  React.useEffect( () => {
  AsyncStorage.getItem('volume').then(savedVolume => setVolume(savedVolume as unknown as string))
  }, []);

  



  const changeVolume = async (volume: SetStateAction<string>) => {
    setVolume(volume);

    try {
      await AsyncStorage.setItem(
        'volume',
        volume as unknown as string
      );
    } catch (error: any) {
      console.log('Error saving data ', (error as unknown as Error).message)
    }

  }

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Volume</Text>
      <TextInput
        style={styles.input}
        onChangeText={ changeVolume}
        value={volume}
        placeholder="set volume"
        keyboardType="numeric"
      />
    </View>
  );
}

const Tab = createBottomTabNavigator();

export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator>
        <Tab.Screen name="Home" component={HomeScreen} />
        <Tab.Screen name="Settings" component={SettingsScreen} />
        <Tab.Screen name="About" component={AboutScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 0,
    flexDirection: 'row'
  },
  input: {
    height: 40,
    margin: 12,
    borderWidth: 1,
    padding: 10,
  },
  text: {
    height: 40,
    margin: 12,
    padding: 10,
    fontWeight: 'bold'
  },
  about: {
    margin: 0,
    padding: 20,
    justifyContent: 'center', //Centered horizontally
    alignItems: 'center', //Centered vertically
    flex:1,
    fontSize: 18
  },
});