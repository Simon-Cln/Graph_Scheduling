declare module 'react-vis-network-graph' {
    import { Component } from 'react';
  
    interface NetworkProps {
      graph: {
        nodes: Array<{
          id: string;
          label: string;
          title?: string;
          color?: {
            background?: string;
            border?: string;
            highlight?: {
              background?: string;
              border?: string;
            };
          };
          [key: string]: any;
        }>;
        edges: Array<{
          from: string;
          to: string;
          label?: string;
          color?: {
            color?: string;
            highlight?: string;
          };
          [key: string]: any;
        }>;
      };
      options?: {
        nodes?: {
          shape?: string;
          size?: number;
          font?: {
            face?: string;
            size?: number;
          };
          borderWidth?: number;
          color?: {
            background?: string;
            border?: string;
            highlight?: {
              background?: string;
              border?: string;
            };
          };
        };
        edges?: {
          arrows?: {
            to?: {
              enabled?: boolean;
              scaleFactor?: number;
            };
          };
          color?: {
            color?: string;
            highlight?: string;
          };
          font?: {
            face?: string;
            size?: number;
          };
          width?: number;
        };
        physics?: {
          enabled?: boolean;
          hierarchicalRepulsion?: {
            centralGravity?: number;
            springLength?: number;
            springConstant?: number;
            nodeDistance?: number;
          };
        };
        layout?: {
          hierarchical?: {
            enabled?: boolean;
            direction?: string;
            sortMethod?: string;
            levelSeparation?: number;
          };
        };
      };
    }
  
    export default class Network extends Component<NetworkProps> {}
  }
