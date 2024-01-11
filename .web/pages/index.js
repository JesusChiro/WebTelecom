import { Fragment } from "react"
import { Fragment_fd0e7cb8f9fb4669a6805377d925fba0 } from "/utils/stateful_components"
import { Center, HStack, Image, Menu, MenuButton, Spacer, VStack } from "@chakra-ui/react"
import "focus-visible/dist/focus-visible"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <Fragment_fd0e7cb8f9fb4669a6805377d925fba0/>
  <Fragment>
  <Center sx={{"paddingX": "4em", "paddingY": "1em", "backgroundColor": "#52D3D8", "position": "fixed", "top": "0px", "zIndex": "999", "width": "100%"}}>
  <HStack>
  <Image src={`logo.png`} sx={{"width": "7em", "height": "4em"}}/>
  <Spacer/>
  <HStack>
  <Menu sx={{"color": "#FFFFFF", "marginX": "7em"}}>
  <MenuButton sx={{"textDecoration": "none", "fontSize": "1.2em", "fontFamily": "Comfortaa", "fontWeight": "500", "_hover": {"color": "#087ec4"}}}>
  {`Nosotros`}
</MenuButton>
  <Spacer/>
  <MenuButton sx={{"textDecoration": "none", "fontSize": "1.2em", "fontFamily": "Comfortaa", "fontWeight": "500", "_hover": {"color": "#087ec4"}}}>
  {`Proyectos`}
</MenuButton>
  <Spacer/>
  <MenuButton sx={{"textDecoration": "none", "fontSize": "1.2em", "fontFamily": "Comfortaa", "fontWeight": "500", "_hover": {"color": "#087ec4"}}}>
  {`Principales Clientes`}
</MenuButton>
  <Spacer/>
  <MenuButton sx={{"textDecoration": "none", "fontSize": "1.2em", "fontFamily": "Comfortaa", "fontWeight": "500", "_hover": {"color": "#087ec4"}}}>
  {`Contactenos`}
</MenuButton>
</Menu>
</HStack>
</HStack>
</Center>
  <VStack>
  <VStack/>
</VStack>
</Fragment>
  <NextHead>
  <title>
  {`NMT`}
</title>
  <meta content={`A Reflex app.`} name={`description`}/>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
