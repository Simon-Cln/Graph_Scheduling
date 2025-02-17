import React, { useEffect, useRef } from 'react';
import { Network } from 'vis-network';
import { Box } from '@mui/material';
import { GraphData, Node, Edge } from '../types/graphTypes';

interface GraphDisplayProps {
    data: GraphData;
    zoom?: number;
    viewMode?: 'timeline' | 'tree';
    showCriticalPath?: boolean;
}

const GraphDisplay: React.FC<GraphDisplayProps> = ({ 
    data, 
    zoom = 1, 
    viewMode = 'timeline',
    showCriticalPath = false 
}) => {
    const networkRef = useRef<HTMLDivElement>(null);
    const network = useRef<Network | null>(null);

    useEffect(() => {
        if (!networkRef.current || !data) return;

        const nodes = data.graph.nodes.map(node => ({
            id: node.id.toString(),
            label: `Tâche ${node.label}\n
                   Durée: ${node.duration}\n
                   Date au plus tôt: ${node.early_date}\n
                   Date au plus tard: ${node.late_date}\n
                   Marge totale: ${node.total_margin}\n
                   Marge libre: ${node.free_margin}`,
            color: {
                background: data.criticalPath.includes(node.id) ? '#ff7675' : '#74b9ff',
                border: data.criticalPath.includes(node.id) ? '#d63031' : '#0984e3',
                highlight: {
                    background: data.criticalPath.includes(node.id) ? '#fab1a0' : '#a0d8ef',
                    border: data.criticalPath.includes(node.id) ? '#ff7675' : '#74b9ff'
                }
            }
        }));

        const edges = data.graph.edges.map(edge => ({
            from: edge.from.toString(),
            to: edge.to.toString(),
            arrows: 'to',
            color: {
                color: data.criticalPath.includes(edge.from) && 
                      data.criticalPath.includes(edge.to) ? '#d63031' : '#0984e3'
            }
        }));

        const options = {
            nodes: {
                shape: 'box',
                margin: {
                    top: 10,
                    right: 10,
                    bottom: 10,
                    left: 10
                },
                widthConstraint: {
                    minimum: 100,
                    maximum: 200
                },
                font: {
                    size: 14,
                    multi: true,
                    face: 'arial'
                }
            },
            edges: {
                width: 2,
                smooth: {
                    enabled: true,
                    type: viewMode === 'timeline' ? 'curvedCW' : 'cubicBezier',
                    roundness: 0.5
                }
            },
            layout: {
                hierarchical: viewMode === 'timeline' ? {
                    direction: 'LR',
                    sortMethod: 'directed',
                    levelSeparation: 200,
                    nodeSpacing: 150
                } : false
            },
            physics: viewMode === 'timeline' ? false : {
                barnesHut: {
                    gravitationalConstant: -2000,
                    centralGravity: 0.3,
                    springLength: 200
                }
            }
        };

        network.current = new Network(
            networkRef.current,
            { nodes, edges },
            options
        );

        network.current.once('stabilized', () => {
            if (network.current) {
                network.current.fit();
                network.current.moveTo({
                    scale: zoom
                });
            }
        });

        return () => {
            if (network.current) {
                network.current.destroy();
                network.current = null;
            }
        };
    }, [data, zoom, viewMode, showCriticalPath]);

    return (
        <Box
            ref={networkRef}
            sx={{
                width: '100%',
                height: '100%',
                bgcolor: 'background.paper',
                borderRadius: 1,
                overflow: 'hidden'
            }}
        />
    );
};

export default GraphDisplay;
